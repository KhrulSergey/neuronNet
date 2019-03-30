input layer
% adding bias
a1 = [ones(m, 1) X];

% hidden layer
z2 = a1 * Theta1';
a2 = sigmoid(z2);
% adding bias
a2 = [ones(size(z2, 1), 1) a2];

% output layer
z3 = a2 * Theta2';
a3 = sigmoid(z3);

% prediction
[a, p] = max(a3');
p = p';


