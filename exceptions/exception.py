import sys

class CoffeePipelineException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(error)
        self.error_detail = error_detail

    def __str__(self):
        _, _, tb = self.error_detail.exc_info()
        file_name = tb.tb_frame.f_code.co_filename
        line_number = tb.tb_lineno
        return f"Error in file [{file_name}] at line [{line_number}]: {self.args[0]}"
