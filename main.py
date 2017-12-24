#!/usr/bin/env python3

import sys

__author__ = "mynameajeff"

class StupidIdea:

    def __init__(self, script_string):

        with open(script_string, "r") as fl:
            self.scriptstr = ''.join(
                [line for line in fl]
            )[::-1][1:].split("\n")

        for i, line in enumerate(self.scriptstr):
            if ";" in line:
                temp_variable = self.scriptstr[i].split(";")
                del self.scriptstr[i]

                for z in range(len(temp_variable)):
                    self.scriptstr.insert(i+z, temp_variable[z])

                isSemi = True
                break

            else:
                isSemi = False

        if not isSemi:
            if len(self.scriptstr) == 1:
                self.scriptstr = list(self.scriptstr)

        self.ERROR_CODES = {
            "NOSTART" : (170, "NO START CHARACTER GIVEN"),
            "MULSTONLN" : (171, "MULTIPLE STATEMENTS ON ONE LINE"),
            "INVSYNTAX" : (172, "MALFORMED SYNTAX GIVEN WITHIN STATEMENT")
        }

        self.stack = []

        self.skip_len = 0

        self.STATEMENT_COMPLETE = False

    def ERROR_HANDLER(self, errsig):

        print("INVALID CODE {a[0]}; {a[1]}."
            .format(a = self.ERROR_CODES[errsig]))
        sys.exit()

    def check_token(self):

        if self.token in ("<", "/"):
            token_before = self.statement[self.token_index - 1]
            token_after  = self.statement[self.token_index + 1]

            if self.STATEMENT_COMPLETE:
                self.ERROR_HANDLER("MULSTONLN")

        if self.token == "<":

            if token_before == "s":
                if token_after == "'":

                    if "\"" in self.statement:
                        for i, x in enumerate(self.statement):
                            if x == "\"":
                                endofstr_index = i
                                break

                    newstr = self.statement[self.token_index + 2:endofstr_index][::-1] \
                        .replace("\\n", "\n") \
                        .replace("\\'", "\'")

                    self.stack.append([char for char in newstr])

                    self.skip_len += len(newstr) + 3

                    self.STATEMENT_COMPLETE = True

        elif self.token == "/":

            if token_before == "s":
                if token_after == ".":

                    if len(self.stack) > 0:
                        for ind, char_to_push in enumerate(self.stack[0]):
                            print(char_to_push, end = "")
                            del char_to_push

                        del self.stack[0]

                        self.STATEMENT_COMPLETE = True

                else:
                    self.ERROR_HANDLER("INVSYNTAX")

            elif token_before == ",":
                if token_after == "s":

                    temp = input()

                    self.stack.append([char for char in temp])
                else:
                    self.ERROR_HANDLER("INVSYNTAX")
            else:
                self.ERROR_HANDLER("INVSYNTAX")

    def parse(self):

        if self.scriptstr[0][0] != ":":
            self.ERROR_HANDLER("NOSTART")

        for self.statement in self.scriptstr:

            for self.token_index, self.token in enumerate(self.statement):

                if self.skip_len != 0:
                    self.skip_len -= 1
                    continue

                self.check_token()

            if self.STATEMENT_COMPLETE:

                self.STATEMENT_COMPLETE = False
                continue

if __name__ == "__main__":

    instance = StupidIdea("stupidexample.si")
    instance.parse()
