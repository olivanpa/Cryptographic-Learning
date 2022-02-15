% Read Original Image
X = imread('test.jpg');
Y = rgb2gray(X);
figure(1);
imshow(Y);
% SVD
[U,D,V] = svd(double(Y))
SS = size(D);
M = zeros(SS(1), SS(2));
H = min(SS(1), SS(2));
dd = fix(H/9);
d = fix(sqrt(dd));
for L = 1:d*d
    MM = M;
    % Get Minor Component
    for ii = 1:(L)*9 + 9
        MM(SS(1)-ii+1, SS(1)-ii+1) = 1;
    end
    rho = SS(1)*SS(2)/((SS(1)+SS(2)+1)*L);
    % Rebuild
    GG = U*(MM.*D)*V';
    iG  =  imcomplement(GG);
    figure(3),subplot(d, d, L),
    imshow(uint8(iG));
    title(['L = ',num2str(L*9+9),', rho = ',num2str(rho)]);
end
ZZ = zeros(d,d);
flag = 1;
for ii = 1:d
    for jj = 1:d
        ZZ(ii,jj) = abs(D(flag,flag));
        flag = flag+1;
    end
end
disp(ZZ);