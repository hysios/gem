#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


'''
 * GeM - Gait-phase Estimation Module
 *
 * Copyright 2018-2020 Stylianos Piperakis, Foundation for Research and Technology Hellas (FORTH)
 * License: BSD
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the Foundation for Research and Technology Hellas (FORTH) 
 *	 nor the names of its contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
'''


from math import exp, sqrt

class Gaussian():
	def __init__(self):
		pass

    # return pdf(x, mu, signma) = Gaussian pdf with mean mu and stddev sigma
	#if mu and sigma are not defined return the standard Gaussian pdf
	def pdf(self,x, mu = None, sigma = None):
		if(mu == None and sigma == None):
			return exp(-x*x / 2.00) / sqrt(2 * 3.141592653589793238463)
		else:
			x= (x - mu) / sigma
			return (exp(-x*x / 2.00) / sqrt(2 * 3.141592653589793238463))/sigma


    # return cdf(z, mu, sigma) = Gaussian cdf with mean mu and stddev sigma
	#if mu and sigma are not defined return the standard Gaussian cdf
	def cdf(self,z, mu = None, sigma = None):
		if(mu != None and sigma != None):
			z = (z - mu)/sigma

		if(z < -8.0):
			return 0.0
		if(z >  8.0):
			 return 1.0
        
		sum = 0.0
		term = z
		i=3
		while(sum+term !=sum):
			sum  = sum + term
			term = term * z * z / i
			i=i+2

		return 0.5 + sum * self.pdf(z)