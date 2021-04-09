d = 10^3:1:10^5;
PL1 = -20*log10(1./(16*pi*d));
ht = 40;
hr = 1.5;
PL2 = -10*log10(ht^2*hr^2./d.^4);
PL3 = 69.55+26.16*log10(1.2*10^9)-13.82*log10(ht)-3.2*(log10(11.75*hr))^2-4.97+5*randn(size(d));
semilogx(d,PL1,d,PL2,d,PL3);
legend('Friis Law','Ground-Reflection Model','Hata with shadowing')
xlim([1000,10^5])