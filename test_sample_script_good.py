import collections

import sample_script_good


def test_run_under_threshold():
    FakeArgs = collections.namedtuple('FakeArgs', ['offset'])
    fake_args = FakeArgs(offset=0)
    num = sample_script_good.run(offset=fake_args.offset)
    assert isinstance(num, int)


def test_run_over_threshold():
    FakeArgs = collections.namedtuple('FakeArgs', ['offset'])
    fake_args = FakeArgs(offset=11)
    num = sample_script_good.run(offset=fake_args.offset)
    assert isinstance(num, int)
