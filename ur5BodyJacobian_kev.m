function [Jbst] = ur5BodyJacobian_kev(Q)

%grab first portion of ur5FwdKin.m
if size(Q,1) ~=6 || size(Q,2) ~= 1
    error('Size of intput q should be 6x1; Check your q dimensions')
end

% Define the link length 
L0 = 89.2e-3;
L1 = 425e-3;    
L2 = 392e-3;
L3 = 109.3e-3;
L4 = 94.75e-3;
L5 = 82.5e-3;   

% Define w
e2 = [0;1;0];
e3 = [0;0;1];

w1 = e3;
w2 = e2;
w3 = e2;
w4 = e2;
w5 = e3;
w6 = e2;
w=[w1,w2,w3,w4,w5,w6];

% Define q
q1 = [0; 0; 0];
q2 = [0; 0; L0];
q3 = [0; 0; L0+L1];
q4 = [0; 0; L0+L1+L2]; 
q5 = [0; L3; 0];
q6 = [0; L3+L5; L0+L1+L2+L4];
q=[q1,q2,q3,q4,q5,q6];

% Calculate Xi_hat
Xi_hat = cell(6, 1);

Xi_hat{1} = [[SKEW3(w1), -cross(w1, q1)]; [0, 0, 0, 0]];
Xi_hat{2} = [[SKEW3(w2), -cross(w2, q2)]; [0, 0, 0, 0]];
Xi_hat{3} = [[SKEW3(w3), -cross(w3, q3)]; [0, 0, 0, 0]];
Xi_hat{4} = [[SKEW3(w4), -cross(w4, q4)]; [0, 0, 0, 0]];
Xi_hat{5} = [[SKEW3(w5), -cross(w5, q5)]; [0, 0, 0, 0]];
Xi_hat{6} = [[SKEW3(w6), -cross(w6, q6)]; [0, 0, 0, 0]];

% Define gst(0)
gst0 = [ROTX(-pi/2), [0, L3+L5, L0+L1+L2+L4]';0 0 0 1];

g=eye(4);

%calculating gst
for i=1:6
    g = g * expm(Q(i)*Xi_hat{i});
end

gst=g*gst0;

% calculate Spatial Jacobian first
% a row of screws so a 6 x 6 grab Xi_hat into arrays
xi_array = zeros(6,6);

for i = 1:6
    xi_array(:,i) = [-cross(w(:,i),q(:,i));w(:,i)];           
end

% now calculate jacobian
Jsst = zeros(6);
%pre-defining Jsst screw 1 since it does not change
Jsst(:,1) = xi_array(:,1); % 11/2 notes

for i = 2:6
    % reset values for g
    g = eye(4);
    for j = 1:i-1
        g = g * expm(Q(i)*Xi_hat{i});
    end
    
    %adj for g
    adj_g=[g(1:3,1:3),SKEW3(g(1:3,4))*g(1:3,1:3);zeros(3),g(1:3,1:3)];
    Jsst(:,i) = adj_g*xi_array(:,i);        
end

% grab gst now and write out a adj for gst
ad_gst = [gst(1:3,1:3),SKEW3(gst(1:3,4))*gst(1:3,1:3);zeros(3),gst(1:3,1:3)];
Jbst = ad_gst\Jsst;

end

