"""动画状态机：转移、条件与层：待实现的核心模块。"""


def transition_allowed(current, transitions):
    """按当前状态查转移表。"""
    raise NotImplementedError

def condition_eval(conditions, params):
    """条件全匹配。"""
    raise NotImplementedError

def blend_weights(weights):
    """混合权重归一化。"""
    raise NotImplementedError

def interrupt_priority(priority, current_priority):
    """打断优先级比较。"""
    raise NotImplementedError

def event_emit(state, events):
    """事件按状态派发。"""
    raise NotImplementedError

def layer_mask(layer, mask):
    """层遮罩位运算。"""
    raise NotImplementedError

def sync_phase(phase, speed, dt):
    """同步相位取模。"""
    raise NotImplementedError

def cooldown_ready(last_time, now, cooldown):
    """冷却按时间差。"""
    raise NotImplementedError

def cache_key(machine, state):
    """缓存键含状态机名。"""
    raise NotImplementedError

def commit_states(statuses):
    """批量状态全部成功才提交。"""
    raise NotImplementedError
