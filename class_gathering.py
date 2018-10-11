import numpy as np

class gathering:


	def __init__(self, t_max):
		"""
		Input: t_max (int).
		-----
		Output: None.
		-----
		Comment: Constructor. Takes as self parameter t_max.
		-----
		"""
		self.t_max = t_max


	def minute_bin(self, t, s,):
		"""
		Input: t (array), s (array).
		-----
		Output: s_minute (array).
		-----
		Comment: Takes the data; s the survival function and t the time
		in hours and returns s_minute, a minute-bin array containing s.
		-----
		"""
		s_minute = np.arange(0, self.t_max, 1) * 0

		s_minute[0] = s[0]

		for i in range(len(s_minute)-1):
			for j in range(len(t)):
				if (t[j]*60 >= i) and (t[j]*60 < i+1):
					s_minute[i] = s[j]
		for i in range(len(s_minute)-1):
			if s_minute[i+1] == 0:
				s_minute[i+1] = s_minute[i]

		for i in range(len(s)):
			if s[i] == 0:
				i_end = i
				break

		for i in range(len(s_minute)):
			if i > t[i_end]*60:
				s_minute[i] = 0
		return s_minute
