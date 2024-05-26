# ei_ce.py
import numpy as np

def eigenvector_centrality(A, alpha=0.85, tol=1e-6, max_iter=100):
    """
    Computes the eigenvector centrality of nodes in a graph.

    Args:
    A (numpy.ndarray): Adjacency matrix of the graph.
    alpha (float): Damping factor (default: 0.85).
    tol (float): Tolerance to determine convergence (default: 1e-6).
    max_iter (int): Maximum number of iterations (default: 100).

    Returns:
    numpy.ndarray: Eigenvector centrality vector.
    """
    n = A.shape[0]
    c = np.ones(n) / n  # Initialize centrality vector with equal values
    A_T = A.T  # Transpose of the adjacency matrix
    
    for _ in range(max_iter):
        c_next = alpha * np.dot(A_T, c) + (1 - alpha) * np.ones(n) / n
        c_next /= np.linalg.norm(c_next, 1)  # Normalize centrality vector
        if np.linalg.norm(c_next - c, 1) < tol:
            break  # Convergence criteria met
        c = c_next  # Update centrality vector
    
    return c


def normalize(vector):
    """
    Normalizes the input vector.

    Args:
    vector (numpy.ndarray): Input vector to be normalized.

    Returns:
    numpy.ndarray: Normalized vector.
    """
    norm = np.linalg.norm(vector, 1)
    return vector / norm if norm != 0 else vector

def calculate_combined_weight(A, C, I, alpha, beta, gamma):
    """
    Calculates the combined weight vector using eigenvector centrality,
    click-through rates (CTR), and impressions.

    Args:
    A (numpy.ndarray): Adjacency matrix representing the internal linking structure.
    C (numpy.ndarray): Vector of click-through rates (CTR) for each page from search results.
    I (numpy.ndarray): Vector of impressions for each page from search results.
    alpha (float): Damping factor for the eigenvector centrality component.
    beta (float): Weight for the CTR component.
    gamma (float): Weight for the impressions component.

    Returns:
    numpy.ndarray: Combined weight vector.
    """
    # Calculate eigenvector centrality
    centrality = eigenvector_centrality(A, alpha)

    # Normalize C and I
    C_norm = normalize(C)
    I_norm = normalize(I)

    # Calculate combined weight
    weights = alpha * centrality + beta * C_norm + gamma * I_norm

    return weights
