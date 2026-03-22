history = []
failures = []


def log(step):
    history.append(step)
    if "error" in step.get("result", "").lower() or "failed" in step.get("result", "").lower():
        failures.append(step)


def get_history():
    return history


def get_failures():
    return failures
