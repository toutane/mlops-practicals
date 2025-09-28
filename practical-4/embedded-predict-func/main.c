#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "ml_func.h"

#define NB_PARAMS 3
#define THRESHOLD 0.00001

void test_linear_regression_prediction(void)
{
    float features[NB_PARAMS] = {1, 1, 1};
    float thetas[] = {0, 1, 1, 1};
    float y_pred;

    y_pred = linear_regression_prediction(features, thetas, NB_PARAMS);
    assert(y_pred == 3.0);
}

void test_exp_approx(void)
{
    assert(exp_approx(0., 5) == 1);
    assert(fabs(exp_approx(1, 5) - 2.716667) < THRESHOLD);
}

void test_sigmoid(void)
{
    assert(sigmoid(4) > 0.9);
    assert(fabs(sigmoid(0.) - 0.5) < THRESHOLD);
}

void test_logistic_regression(void)
{
    float features[NB_PARAMS] = {-1, 1};
    float thetas[] = {0, 1, 1};
    float y_pred;

    y_pred = logistic_regression(features, thetas, NB_PARAMS);
    /* printf("y_pred is: %f\n", y_pred); */
    assert(y_pred == 0.5);
}

void test_simple_tree(void)
{
    float features[] = {1, 1};
    assert(simple_tree(features, 2) == 1);
    features[0] = -1;
    assert(simple_tree(features, 2) == 0);
}

int main(void)
{
    test_linear_regression_prediction();
    test_exp_approx();
    test_sigmoid();
    test_logistic_regression();
    test_simple_tree();
    return 0;
}
