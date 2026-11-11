def reflected_position(distance, left, right):
    """Return the center and heading after travelling distance from the left."""
    span = right - left
    progress = distance % (2 * span)
    if progress < span:
        return left + progress, True
    return right - (progress - span), False
