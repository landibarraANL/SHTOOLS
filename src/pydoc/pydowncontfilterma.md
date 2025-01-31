# DownContFilterMA()

Compute the minimum-amplitude downward continuation filter of Wieczorek and Phillips (1998).

# Usage

wl = DownContFilterMA (l, half, r, d)

# Returns

wl : float, ndarray
:   The amplitude of the downward continuation filter.

# Parameters

l : integer, array_like
:   The spherical harmonic degree.

half : integer, array_like
:   The spherical harmonic degree where the filter is equal to 0.5.

r : float, array_like
:   The reference radius of the gravitational field.

d : float, array_like
:   The radius of the surface to downward continue to.

# Description

DownContFilterMA will calculate the downward continuation filter of Wieczorek and Phillips (1998; eq. 19) as a function of spherical harmonic degree l. The input parameters include half, which is the degree where the filter is equal to 0.5, and r and d, which are the reference radius of the gravitational field and the radius of the surface to downward continue to, respectively.

# References

Wieczorek, M. A. and R. J. Phillips, Potential anomalies on a sphere: applications to the thickness of the lunar crust, J. Geophys. Res., 103, 1715-1724, 1998.
