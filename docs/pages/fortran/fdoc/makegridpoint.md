---
title: MakeGridPoint (Fortran)
keywords: spherical harmonics software package, spherical harmonic transform, legendre functions, multitaper spectral analysis, fortran, Python, gravity, magnetic field
sidebar: fortran_sidebar
permalink: makegridpoint.html
summary:
tags: [fortran]
toc: false
editdoc: fdoc
---

Evaluate a real function expressed in real spherical harmonics at a single point.

## Usage

`value` = MakeGridPoint (`cilm`, `lmax`, `lat`, `lon`, `norm`, `csphase`, `dealloc`)

## Parameters

`value` : output, real(dp)
:   Value of the function at (`lat`, `lon`).

`cilm` : input, real(dp), dimension (2, `lmax`+1, `lmax`+1)
:   The real spherical harmonic coefficients of the function. The coefficients `C1lm` and `C2lm` refer to the cosine (`Clm`) and sine (`Slm`) coefficients, respectively, with `Clm=cilm(1,l+1,m+1)` and `Slm=cilm(2,l+1,m+1)`.

`lmax` : input, integer(int32)
:   The maximum spherical harmonic degree used in evaluating the function.

`lat` : input, real(dp)
:   The latitude of the point in degrees.

`lon` : input, real(dp)
:   The longitude of the point in degrees.

`norm` : input, optional, integer(int32), default = 1
:   1 (default) = Geodesy 4-pi normalized harmonics; 2 = Schmidt semi-normalized harmonics; 3 = unnormalized harmonics; 4 = orthonormal harmonics.

`csphase` : input, optional, integer(int32), default = 1
:   1 (default) = do not apply the Condon-Shortley phase factor to the associated Legendre functions; -1 = append the Condon-Shortley phase factor of (-1)^m to the associated Legendre functions.

`dealloc` : input, optional, integer(int32), default = 0
:   0 (default) = Save variables used in the external Legendre function calls. (1) Deallocate this memory at the end of the funcion call.

## Description

`MakeGridPoint` will expand a function expressed in spherical harmonics at a single point. The input latitude and longitude are in degrees. The employed spherical harmonic normalization and Condon-Shortley phase convention can be set by the optional arguments `norm` and `csphase`; if not set, the default is to use geodesy 4-pi normalized harmonics that exclude the Condon-Shortley phase of (-1)^m.

## See also

[makegridpointc](makegridpointc.html), [makegriddh](makegriddh.html), [makegriddhc](makegriddhc.html), [makegridglq](makegridglq.html), [makegridglqc](makegridglqc.html)
