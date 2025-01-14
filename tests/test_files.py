# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
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

from os import path, remove

from RPC_Test_Common import get_dir_path, reset_to_default_file


def test_load_from_file(mc):
    # This has some differences to the default file so can test it's loaded correctly
    file_path = get_dir_path() + r"\test_files\SaveLoadFiles.mot"
    mc.set_variable("slot_number", 21)
    mc.save_to_file(file_path)

    mc.set_variable("slot_number", 9)
    # make sure slot number has definitely changed
    value = mc.get_variable("slot_number")
    assert value == 9

    # go back to saved file
    mc.load_from_file(file_path)

    # make sure slot number has definitely changed
    value = mc.get_variable("slot_number")
    assert value == 21

    reset_to_default_file(mc)


def test_save_to_file(mc):
    file_path = get_dir_path() + r"\test_files\SaveLoadFiles.mot"

    if path.exists(file_path):
        remove(file_path)

    assert path.exists(file_path) is False

    mc.save_to_file(file_path)

    assert path.exists(file_path) is True

    reset_to_default_file(mc)
