def gradient_matrix(s, dz):
    """Calculate the gradient matrix for 1d linear interpolation.
    Parameters
    ----------
    s : float
        The local coordinate in the element
    dz : float
        The scaling factor from global to local coordinates
    Returns
    -------
    numpy.ndarray, shape = (1, 2)
        The gradient matrix
    """
    return np.array([[-1, 1]]) / dz