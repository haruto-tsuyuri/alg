from typing import Any, Sequence


class Max:
    """
    最大値を保持するクラス
    nums : Sequence
        シークエンス型の整数
    """

    def __init__(self, nums: Sequence) -> None:
        self.nums = nums
        self._max_of()

    def _max_of(self) -> Any:
        """
        コンストラクタの中の最大値を返す
        Returns
        -------
        max_num : Any
            一番大きい整数を返す
        """
        max_num = self.nums[0]
        for num in range(1, len(self.nums)):
            if self.nums[num] > max_num:
                max_num = self.nums[num]
        return max_num
