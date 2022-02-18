# Copyright 2020-2022 The American University in Cairo
# Copyright 2020-2022 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Original Copyright Follows:
# MIT License
#
# Copyright (c) 2019 Hany Moussa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import argparse
from .spef_extractor import SpefExtractor


def main():
    parser = argparse.ArgumentParser(
        description="Create a parasitic SPEF file from def and lef files."
    )

    parser.add_argument("--spef_out", "-o", default=None, help="Output SPEF")

    parser.add_argument("--def_file", "-d", required=True, help="Input DEF")

    parser.add_argument("--lef_file", "-l", required=True, help="Input LEF")

    parser.add_argument(
        "--wire_model", "-mw", default="PI", required=False, help="name of wire model"
    )

    parser.add_argument(
        "--edge_cap_factor",
        "-ec",
        default=1,
        required=False,
        help="Edge Capacitance Factor 0 to 1",
    )

    args = parser.parse_args()

    lef_file_name = args.lef_file
    def_file_name = args.def_file
    wireModel = args.wire_model
    edgeCapFactor = float(args.edge_cap_factor)
    inst = SpefExtractor(edgeCapFactor, wireModel)

    out_file = args.spef_out
    if out_file is None:
        out_file = def_file_name[:-4] + ".spef"

    inst.extract(lef_file_name, def_file_name, wireModel, edgeCapFactor, out_file)


if __name__ == "__main__":
    main()
