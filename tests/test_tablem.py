from hardhat.tablem import TableM

import pytest

def test_charge(brosius, atol) -> None:

     table_m = TableM(
         data=brosius,
         experience='Actual Loss',
         index="Risk"
     )

     assert table_m.phi(r=1.2) == pytest.approx(.21, rel=atol)
     assert table_m.phi(r=1.1) == pytest.approx(.23, rel=atol)