clc;clear;
%%不适用于输入频率都相等的情况
symbols=[1,2,3,4,5,6];
p1=[0.21,0.1,0.3,0.09,0.25,0.05];
dict=cell(length(p1),2);
for i=1:length(p1)
    dict{i,1}=strcat('x',num2str(i));
end
p2=sort(p1);
p=sort(p1);
cum=cell(length(p)-1,1);
cum{1}=p;
while length(p)>2
    p(2)=p(1)+p(2);
    p(1)=[];
    p=sort(p);
    cum{length(p1)-length(p)+1}=p;
end
a=cell(cum);%%储存code
for i=length(cum):-1:1
    if i==length(cum)
        big=max(cum{i});
        small=min(cum{i});
        index_big=find(cum{i}==big);
        index_small=find(cum{i}==small);
        if length(index_big)==2
            index_big = 1;
            index_small = 2;
        end
        a{i,index_big}='0';
        a{i,index_small}='1';
        
    else
        same = intersect(cum{i+1},cum{i});%%找相同元素
        for j=1:length(same)
            arg=find(cum{i}==same(j));
            arg1=find(cum{i+1}==same(j));
            a{i,arg}=a{i+1,arg1};%%same keeps the same
        end
        diff = sort(setxor(same,cum{i}));%sort here
        diff_1=sum(diff);
        for j=1:length(diff)
            arg=find(cum{i}==diff(j));
            arg1=find(cum{i+1}==diff_1);
            if j==1
                a{i,arg}=[a{i+1,arg1},'1'];%add 1/0,小的
            else
                a{i,arg}=[a{i+1,arg1},'0'];
            end
        end
    end
end

for i=1:6
    fprintf('x%d',7-i)
    fprintf(' ')
    disp(a{1,i})
    L(i)=length(a{1,i});
end
p=p2
L_avg=sum(p.*L);
disp('平均码长');
disp(L_avg);
H=sum(-p.*log2(p));
eta=H/L_avg;
disp('效率');
disp(eta)
    
    
