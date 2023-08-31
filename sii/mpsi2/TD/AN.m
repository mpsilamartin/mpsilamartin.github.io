clear all
close all

L1=0.405;
L2=0.433;
L3=1.075;
L4=1.762;
L5=0.165;
L6=0.25;
L8=0.75;
t10=[0,0]*pi/180;
t21=[58,-58]*pi/180;
t31=[25,-35]*pi/180;
t43=[0,0]*pi/180;
t51=[-90,90]*pi/180;

x=L1+L3*cos(t21)+L4*cos(t31)-L5*sin(t31)+L6*cos(t31)+L8*cos(t51)
y=L2+L3*sin(t21)+L4*sin(t31)+L5*cos(t31)+L6*sin(t31)+L8*sin(t51)
y(1)-y(2)

O0=[[0,0];[0,0]]
O2=[[L1,L2];[L1,L2]]
O3=[L3*cos(t21)',L3*sin(t21)']+O2
O4=[L4*cos(t31)'-L5*sin(t31)',L4*sin(t31)'+L5*cos(t31)']+O3
O5=[L6*cos(t31)',L6*sin(t31)']+O4
P=[L8*cos(t51)',L8*sin(t51)']+O5


%Def du cercle du fuselage
R=1.17;
O=[2.7,(y(1)+y(2))*0.5];
t=[90:270]*pi/180;
xc=[O(1)+R*cos(t)];
yc=[O(2)+R*sin(t)];

figure
lstyle={'-','--'}
for k=[1,2]
plot([O0(k,1),O2(k,1)],[O0(k,2),O2(k,2)],'r','LineWidth',3,'LineStyle',lstyle{1,k},'MarkerSize',10)
hold on
plot([O2(k,1),O3(k,1)],[O2(k,2),O3(k,2)],'b','LineWidth',3,'LineStyle',lstyle{1,k})
plot([O3(k,1),O4(k,1)],[O3(k,2),O4(k,2)],'g','LineWidth',3,'LineStyle',lstyle{1,k})
plot([O4(k,1),O5(k,1)],[O4(k,2),O5(k,2)],'m','LineWidth',3,'LineStyle',lstyle{1,k})
plot([O5(k,1),P(k,1)],[O5(k,2),P(k,2)],'k','LineWidth',3,'LineStyle',lstyle{1,k})
plot([O2(k,1)],[O2(k,2)],'ro','LineWidth',3,'MarkerSize',20,'LineStyle',lstyle{1,k})
plot([O3(k,1)],[O3(k,2)],'bo','LineWidth',3,'MarkerSize',20,'LineStyle',lstyle{1,k})
plot([O5(k,1)],[O5(k,2)],'mo','LineWidth',3,'MarkerSize',20,'LineStyle',lstyle{1,k})
end

plot(xc,yc,'k-','LineWidth',5) 
axis equal



