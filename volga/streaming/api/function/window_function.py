from abc import abstractmethod
from typing import  Any, Collection

from volga.streaming.api.function.aggregate_function import AllAggregateFunction
from volga.streaming.api.function.function import Function
from volga.streaming.api.message.message import Record


class WindowFunction(Function):

    @abstractmethod
    def apply(self, elems: Collection[Record]) -> Any:
        pass


class AllAggregateApplyWindowFunction(WindowFunction):

    def __init__(self, all_agg_func: AllAggregateFunction):
        self.all_agg_func = all_agg_func
        self.acc = None

    def apply(self, records: Collection[Record]) -> AllAggregateFunction._Acc:
        if self.acc is None:
            self.acc = self.all_agg_func.create_accumulator()
        for r in records:
            self.all_agg_func.add(r, self.acc)

        return self.acc

