close all;clear;
N=2048*128;%nums
fs=2048*30000;%sample rate
fc=28*10^9;%carrier freq
dt=1/fs;
t=0:dt:((N-1)*dt);
M=32;%path nums
a=rand(1,M);
a=a/sqrt(sum(a.^2));
phi=rand(1,M)*2*pi;
It=0;Qt=0;
fd=3000;%doppler freq
%gama=rand(1,M)*2*pi;

gama=2*pi/M;
%phi=2*pi/M;
for i=1:M
    It=It+a(i)*cos(2*pi*fd*cos(gama*i)*t+phi(i)+fc*t*2*pi);
    Qt=Qt+a(i)*sin(2*pi*fd*cos(gama*i)*t+phi(i)+fc*t*2*pi);
end
rt=It+1i*Qt;

figure;
plot(t,angle(rt));
title('相位增益')
%rt=It.*cos(2*pi*fc.*t)-Qt.*sin(2*pi*fc.*t);
r_out=abs(rt);
figure;
plot(t,10*log10(r_out))
title('rayleigh atennuation r(t)')
xlabel('t/s')
ylabel('signal amplitute/dB')
auto_corr=xcorr(rt,rt);
auto_corr=auto_corr/max(abs(auto_corr));
figure;
plot(t,abs(auto_corr(N:end)))
title('autocorrelation ')
Classical_corr=besselj(0,2*pi*fd*t);
hold on;
plot(t,abs(Classical_corr));
legend('real','imagine')
xlabel('\tau/s')
ylabel('R(\tau)')
%figure;hist(r_out,100)
figure;[f,xi]=ksdensity(abs(rt));
plot(xi,f);
title('amplitude cdf')
%figure;plot(angle(rt)/3.14*pi)
[f,xi]=ksdensity(angle(rt));
figure;
plot(xi,f);
title('phase cdf')
% doppler=fftshift(fft(abs(auto_corr(N:end)))/N);
% doppler1=fftshift(fft(abs(Classical_corr)/N));
% figure;
% %f=(-N+1:N-1)/N*fd+fc;
% f=(-N/2:N/2-1)/N*2*fd+fc;
% plot(f,abs(doppler))
% axis([2.79999999996*10^10 2.80000000004*10^10 0 0.1])
% hold on
% f=(-N/2:N/2-1)/N*2*fd+fc;
% plot(f,abs(doppler1))
% legend('real','theoretial')
% title('doppler spectrum')
%axis([1.3*10^5 1.32*10^5 0 0.5])

fp=(-N/2:N/2-1)/N*2*fd+fc;
P=abs((fft(abs(auto_corr(N:end)))));
%[f,xi]=ksdensity(P);
figure;
%plot(xi,f);
plot(fp,10*log10(P))
hold on;
power=abs((fft(Classical_corr)));
%[f,xi]=ksdensity(P);
%plot(xi,f);
plot(fp,10*log10(power))
title('doppler ')
legend('real','theoretial')
