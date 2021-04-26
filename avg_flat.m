clear;close all;
N=2048*128;%nums
fs=2048*30000;%sample rate
dt=1/fs;
t=0:dt:((N-1)*dt);
fd=3000;%doppler freq
M=32;%path nums
fc=28*10^9;%carrier freq

W=10;
It=zeros(W,N);Qt=zeros(W,N);
rt=It+1i*Qt;
r_out=abs(rt);

for k=1:W
a(k,:)=rand(1,M);
a(k,:)=a(k,:)/sqrt(sum(a(k).^2));
phi(k,:)=rand(1,M)*2*pi;


gama(k,:)=rand(1,M)*2*pi;
for i=1:M
    It(k,:)=It(k,:)+a(k,i)*cos(2*pi*fd*cos(gama(k,i))*t+phi(k,i)+fc*t*2*pi);
    Qt(k,:)=Qt(k,:)+a(k,i)*sin(2*pi*fd*cos(gama(k,i))*t+phi(k,i)+fc*t*2*pi);
end
rt(k,:)=It(k,:)+1i*Qt(k,:);
r_out(k,:)=abs(rt(k,:));
end
rt=mean(rt);
r_out=mean(r_out);

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
hold on;
sigma=sqrt(mean(r_out.^2));
theo_amp=xi/(sigma^2).*exp(-xi.^2/(sigma^2));
plot(xi,theo_amp)
legend('real','theoretial')
title('amplitude pdf')

[f,xi]=ksdensity(angle(rt));
figure;
plot(xi,f);
hold on;
ang=1/2/pi*ones(size(xi));
plot(xi,ang)
legend('real','theoretial')
title('phase pdf')
%fp=t/max(t)*fs;
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



[f,xi]=ksdensity(10*log10(P));
figure;
plot(xi,f);
xlim([0 10^2])
[f,xi]=ksdensity(10*log10(power));
hold on;
plot(xi,f);
xlim([0 10^2])
title('功率谱密度分布')%%是求多普勒普的分布函数
legend('real','theoretical')