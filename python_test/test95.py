import numpy as np
from scipy.signal import convolve2d

def cng(obs):
        """
        Generates a compressed grid where each cell contains the mean value
        of itself and its neighbors in the normal grid. Cells originally
        corresponding to holes (value 1) are set to zero.

        The result is stored in self.compressed_grid as a NumPy array of
        shape (1, H, W), dtype float32.

        Returns
        -------
        None
        """

        # Remove the channel dimension for easier computation
        grid = obs[0]

        # Create hole mask
        hole_mask = (grid == 1.0)

        # Convolution kernel for summing 3x3 neighborhood
        kernel = np.ones((3, 3), dtype=np.float32)

        # Sum of neighbors (using convolution)
        sum_neighbors = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)

        # Count how many valid cells contribute to each sum
        ones_grid = np.ones_like(grid, dtype=np.float32)
        count_neighbors = convolve2d(ones_grid, kernel, mode='same', boundary='fill', fillvalue=0)

        # Calculate mean
        mean_grid = np.round(sum_neighbors / count_neighbors, 2)

        # Set cells corresponding to holes to zero
        mean_grid[hole_mask] = 0.0

        # Add channel dimension back
        return mean_grid[np.newaxis, :, :]

obs = np.array([[[2, 2, 2, 2, 1, 2, 2, 2],
                 [2, 2, 2, 2, 2, 2, 1, 2],
                 [2, 2, 2, 1, 1, 1, 2, 2],
                 [2, 2, 2, 2, 1, 1, 2, 1],
                 [2, 2, 2, 2, 2, 2, 2, 1],
                 [2, 1, 1, 2, 2, 2, 1, 2],
                 [1, 1, 2, 2, 1, 2, 1, 2],
                 [2, 2, 2, 1, 2, 2, 2, 3]]])

a = cng(obs)
print(a)
