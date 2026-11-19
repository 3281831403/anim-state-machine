import pytest

from animation import state_machine as mod

CASES = [
    ('transition_allowed', ['idle', {'idle': 'run'}], 'run', False),
    ('transition_allowed', ['run', {'idle': 'run'}], None, False),
    ('condition_eval', [{'hp': 0}, {'hp': 0, 'mp': 1}], True, False),
    ('condition_eval', [{'hp': 0}, {'hp': 1}], False, False),
    ('blend_weights', [[1, 1, 2]], [0.25, 0.25, 0.5], True),
    ('interrupt_priority', [3, 2], True, False),
    ('interrupt_priority', [1, 2], False, False),
    ('event_emit', ['attack', {'attack': ['hit']}], ['hit'], False),
    ('layer_mask', [5, 3], 1, False),
    ('sync_phase', [0.9, 1.0, 0.2], 0.10000000000000009, True),
    ('cooldown_ready', [10, 12, 1], True, False),
    ('cache_key', ['hero', 'idle'], 'hero:idle', False),
    ('commit_states', [[True, True]], True, False),
    ('blend_weights', [[0, 0]], [0.5, 0.5], True),
    ('layer_mask', [2, 1], 0, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_state_machine_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
