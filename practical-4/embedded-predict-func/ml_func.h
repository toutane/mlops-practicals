#ifndef ML_FUNC_H
#define ML_FUNC_H

float linear_regression_prediction(float *features, float *thetas, int n_params);
float exp_approx(float x, int n_term);
float sigmoid(float x);
float logistic_regression(float *features, float *thetas, int n_params);

#endif
