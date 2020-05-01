#!python
#cython: language_level=3
# This file is generated automatically by QuTiP.
# (C) 2011 and later, QuSTaR
import numpy as np
cimport numpy as np
cimport cython
np.import_array()
cdef extern from "numpy/arrayobject.h" nogil:
    void PyDataMem_NEW_ZEROED(size_t size, size_t elsize)
    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)
    void PyDataMem_FREE(void * ptr)
from qutip.cy.interpolate cimport interp, zinterp
from qutip.cy.math cimport erf, zerf
cdef double pi = 3.14159265358979323
from qutip.cy.brtools cimport (dense_add_mult, ZHEEVR, dense_to_eigbasis,
        vec_to_eigbasis, vec_to_fockbasis, skew_and_dwmin,
        diag_liou_mult, spec_func, farray_alloc)
from qutip.cy.brtools cimport (cop_super_mult, br_term_mult)
include '/usr/local/lib/python3.7/site-packages/qutip/cy/complex_math.pxi'

cdef double[::1] spline1 = np.array([1.8301119700402751e-01,1.6666666666666666e-01,1.5032213632930580e-01,
 1.3596869031139261e-01,1.2288152356585517e-01,1.1108193034398477e-01,
 1.0040790135203606e-01,9.0761560365030511e-02,8.2041421008085369e-02,
 7.4159234335787874e-02,6.7034295674280792e-02,6.0593904496221949e-02,
 5.4772277974446303e-02,4.9509971413898408e-02,4.4753246517525387e-02,
 4.0453529244683546e-02,3.6566912013207269e-02,3.3053705802740987e-02,
 2.9878034734299553e-02,2.7007469750004825e-02,2.4412697447529334e-02,
 2.2067220742329301e-02,1.9947088286216504e-02,1.8030649883105647e-02,
 1.6298335403256765e-02,1.4732454938629220e-02,1.3317018158515133e-02,
 1.2037571020782133e-02,1.0881048171261998e-02,9.8356395240300834e-03,
 8.8906696601309954e-03,8.0364888132038771e-03,7.2643743287836354e-03,
 6.5664415910077724e-03,5.9355635071377906e-03,5.3652977276934634e-03,
 4.8498208589926864e-03,4.3838689962937298e-03,3.9626839702811287e-03,
 3.5819647579794838e-03,3.2378235619169903e-03,2.9267461090316154e-03,
 2.6455557639033962e-03,2.3913810898473324e-03,2.1616265266099469e-03,
 1.9539458852382589e-03,1.7662183894583791e-03,1.5965270189049064e-03,
 1.4431389330483769e-03,1.3044877759153391e-03,1.1791576809018864e-03,
 1.0658688123422900e-03,9.6346429618728035e-04,8.7089840633178446e-04,
 7.8722588595416844e-04,7.1159229481955379e-04,6.4322528397654593e-04,
 5.8142670874707049e-04,5.2556549946935430e-04,4.7507121719210857e-04,
 4.2942822851246029e-04,3.8817044007273321e-04,3.5087653894622187e-04,
 3.1716569030813195e-04,2.8669364845750354e-04,2.5914924147697841e-04,
 2.3425119363273278e-04,2.1174525306582752e-04,1.9140159544376518e-04,
 1.7301247705907107e-04,1.5639011340900854e-04,1.4136476159307270e-04,
 1.2778298694625270e-04,1.1550609620740379e-04,1.0440872122269076e-04,
 9.4377538721274873e-05,8.5310113089959023e-05,7.7113850329527526e-05,
 6.9705052510880909e-05,6.3008063075332965e-05,5.6954494251122435e-05,
 5.1482528696728486e-05,4.6536288239576545e-05,4.2065263263853125e-05,
 3.8023796920551676e-05,3.4370618892466421e-05,3.1068423953739175e-05,
 2.8083491017842060e-05,2.5385338793109779e-05,2.2946414494791920e-05,
 2.0741812564284464e-05,1.8749020040080611e-05,1.6947687783193956e-05,
 1.5319418492164029e-05,1.3847594454790598e-05,1.2517149558842763e-05,
 1.1314632996919968e-05,1.0227259981440416e-05,9.2458113508325668e-06,
 8.3532307118228163e-06,7.5666549604141424e-06,6.7800792090054684e-06],dtype=float)
cdef complex spectral0(double w, double t): return (0.2 * (w >= 0))*(interp(t, 0.0, 10.0, spline1))

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
def cy_td_ode_rhs(
        double t,
        complex[::1] vec,
        complex[::1,:] H0,
        complex[::1,:] C0,
        double[::1] spline0,
        complex[::1,:] A0,
        unsigned int nrows):
    
    cdef double complex * out = <complex *>PyDataMem_NEW_ZEROED(nrows**2,sizeof(complex))
     
    cdef complex[::1, :] H = farray_alloc(nrows)
    cdef complex[::1, :] evecs = farray_alloc(nrows)
    cdef double * eigvals = <double *>PyDataMem_NEW_ZEROED(nrows,sizeof(double))
    dense_add_mult(H, H0, 1)
    ZHEEVR(H, eigvals, evecs, nrows)
    PyDataMem_FREE(&H[0,0])
    cdef double complex * eig_vec = vec_to_eigbasis(vec, evecs, nrows)
    diag_liou_mult(eigvals, eig_vec, out, nrows)
    cop_super_mult(C0, evecs, eig_vec, interp(t, 0.0, 10.0, spline0), out, nrows, 1e-12)
    cdef double[:,::1] skew = <double[:nrows,:nrows]><double *>PyDataMem_NEW_ZEROED(nrows**2,sizeof(double))
    cdef double dw_min = skew_and_dwmin(eigvals, skew, nrows)
    br_term_mult(t, A0, evecs, skew, dw_min, spectral0, eig_vec, out, nrows, 1, 0.1, 1e-12)
    

    cdef np.ndarray[complex, ndim=1, mode='c'] arr_out = vec_to_fockbasis(out, evecs, nrows)
    PyDataMem_FREE(&skew[0,0])
    PyDataMem_FREE(&evecs[0,0])
    PyDataMem_FREE(eigvals)
    PyDataMem_FREE(eig_vec)
    PyDataMem_FREE(out)
    return arr_out
