class Solution(object):
    def maximumEnergy(self, energy, k):
        n = len(energy)
        max_energy = float('-inf')
        
        for i in range(n - 1, -1, -1):
            if i < n - k:
                energy[i] += energy[i + k]
            if energy[i] > max_energy:
                max_energy = energy[i]
        
        return max_energy
