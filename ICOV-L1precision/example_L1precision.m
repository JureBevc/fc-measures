load 20news_w100
docs = double(documents);
sigma = full(docs*docs');%/16242;
disp(size(sigma))
AM = L1precisionBCD(sigma,1);
disp(size(docs));
disp(size(AM));
AM(abs(AM) < 1e-4) = 0;
AM2 = sign(AM);
