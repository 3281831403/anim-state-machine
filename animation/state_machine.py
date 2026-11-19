"""动画状态机：转移、条件与层。"""


def transition_allowed(current, transitions):
    """按当前状态查转移表。"""
    return transitions.get(current)


def condition_eval(conditions, params):
    """条件全匹配。"""
    return all(params.get(key) == value for key, value in conditions.items())


def blend_weights(weights):
    """混合权重归一化。"""
    total = sum(weights)
    if total == 0:
        count = len(weights)
        return [1.0 / count] * count if count else []
    return [weight / total for weight in weights]


def interrupt_priority(priority, current_priority):
    """打断优先级比较。"""
    return priority > current_priority


def event_emit(state, events):
    """事件按状态派发。"""
    return events.get(state, [])


def layer_mask(layer, mask):
    """层遮罩位运算。"""
    return layer & mask


def sync_phase(phase, speed, dt):
    """同步相位取模。"""
    return (phase + speed * dt) % 1.0


def cooldown_ready(last_time, now, cooldown):
    """冷却按时间差。"""
    return now - last_time >= cooldown


def cache_key(machine, state):
    """缓存键含状态机名。"""
    return f"{machine}:{state}"


def commit_states(statuses):
    """批量状态全部成功才提交。"""
    return all(statuses)
