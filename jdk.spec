Summary: Oracle JDK 9

%define prefix /opt/jdk10
%global priority 91000000%{jdk_update}

Name: %{name}
Version: %{version}
Release: %{release}
BuildArch: x86_64
Group: Development/Tools
License: http://java.com/license
URL: http://www.oracle.com/technetwork/java/index.html
Source1: jdk-%{version}_linux-x64_bin.tar.gz
AutoReqProv: no
Provides:   java-sdk-1.10.0 = 1:%{version}
Provides:   java-sdk = 1:1.10.0
Provides:   java-1.10.0-devel = 1:%{version}
Provides:   java-devel = 1:1.10.0
Provides:   jre-1.10.0 = 1:%{version}
Provides:   java-1.10.0 = 1:%{version}
Provides:   jre = 1:1.10.0
Provides:   java = 1:1.10.0
Provides:   java-1.10.0-headless = 1:%{version}
Provides:   java-headless = 1:1.10.0
Provides:   jre-1.10.0-headless = 1:%{version}
Provides:   jre-headless = 1:1.10.0
Provides:   libjvm.so()(64bit)
%global debug_package %{nil}
%define __jar_repack %{nil}

%description
Oracle JDK

%prep
if [ "x$(whoami)" = "xroot" ]; then echo "Do not build as root"; false; fi
%setup -cTn %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}

cd $RPM_BUILD_ROOT%{prefix}

# Install all software without modification
gzip -dc %SOURCE1 | tar xp --strip-components=1
sed -e "s/#crypto.policy=unlimited/crypto.policy=unlimited/" -i conf/security/java.security

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}

%post
alternatives \
  --install %{_bindir}/java java %{prefix}/bin/java %{priority} \
  --slave %{_bindir}/java_vm java_vm %{prefix}/jre/bin/java_vm \
  --slave %{_bindir}/javaws javaws %{prefix}/bin/javaws \
  --slave %{_bindir}/jcontrol jcontrol %{prefix}/bin/jcontrol \
  --slave %{_bindir}/keytool keytool %{prefix}/bin/keytool \
  --slave %{_bindir}/orbd orbd %{prefix}/bin/orbd \
  --slave %{_bindir}/pack200 pack200 %{prefix}/bin/pack200 \
  --slave %{_bindir}/policytool policytool %{prefix}/bin/policytool \
  --slave %{_bindir}/rmid rmid %{prefix}/bin/rmid \
  --slave %{_bindir}/rmiregistry rmiregistry %{prefix}/bin/rmiregistry \
  --slave %{_bindir}/servertool servertool %{prefix}/bin/servertool \
  --slave %{_bindir}/tnameserv tnameserv %{prefix}/bin/tnameserv \
  --slave %{_bindir}/unpack200 unpack200 %{prefix}/bin/unpack200 \
  --slave %{_mandir}/man1/java.1 java.1 %{prefix}/man/man1/java.1 \
  --slave %{_mandir}/man1/keytool.1 keytool.1 %{prefix}/man/man1/keytool.1 \
  --slave %{_mandir}/man1/orbd.1 orbd.1 %{prefix}/man/man1/orbd.1 \
  --slave %{_mandir}/man1/pack200.1 pack200.1 %{prefix}/man/man1/pack200.1 \
  --slave %{_mandir}/man1/policytool.1 policytool.1 %{prefix}/man/man1/policytool.1 \
  --slave %{_mandir}/man1/rmid.1 rmid.1 %{prefix}/man/man1/rmid.1 \
  --slave %{_mandir}/man1/rmiregistry.1 rmiregistry.1 %{prefix}/man/man1/rmiregistry.1 \
  --slave %{_mandir}/man1/servertool.1 servertool.1 %{prefix}/man/man1/servertool.1 \
  --slave %{_mandir}/man1/tnameserv.1 tnameserv.1 %{prefix}/man/man1/tnameserv.1 \
  --slave %{_mandir}/man1/unpack200.1 unpack200.1 %{prefix}/man/man1/unpack200.1
alternatives \
  --install %{_bindir}/javac javac %{prefix}/bin/javac %{priority} \
  --slave %{_bindir}/appletviewer appletviewer %{prefix}/bin/appletviewer \
  --slave %{_bindir}/apt apt %{prefix}/bin/apt \
  --slave %{_bindir}/extcheck extcheck %{prefix}/bin/extcheck \
  --slave %{_bindir}/HtmlConverter HtmlConverter %{prefix}/bin/HtmlConverter \
  --slave %{_bindir}/idlj idlj %{prefix}/bin/idlj \
  --slave %{_bindir}/jar jar %{prefix}/bin/jar \
  --slave %{_bindir}/jarsigner jarsigner %{prefix}/bin/jarsigner \
  --slave %{_bindir}/javadoc javadoc %{prefix}/bin/javadoc \
  --slave %{_bindir}/javah javah %{prefix}/bin/javah \
  --slave %{_bindir}/javap javap %{prefix}/bin/javap \
  --slave %{_bindir}/jconsole jconsole %{prefix}/bin/jconsole \
  --slave %{_bindir}/jdb jdb %{prefix}/bin/jdb \
  --slave %{_bindir}/jhat jhat %{prefix}/bin/jhat \
  --slave %{_bindir}/jinfo jinfo %{prefix}/bin/jinfo \
  --slave %{_bindir}/jmap jmap %{prefix}/bin/jmap \
  --slave %{_bindir}/jps jps %{prefix}/bin/jps \
  --slave %{_bindir}/jrunscript jrunscript %{prefix}/bin/jrunscript \
  --slave %{_bindir}/jsadebugd jsadebugd %{prefix}/bin/jsadebugd \
  --slave %{_bindir}/jstack jstack %{prefix}/bin/jstack \
  --slave %{_bindir}/jstat jstat %{prefix}/bin/jstat \
  --slave %{_bindir}/jstatd jstatd %{prefix}/bin/jstatd \
  --slave %{_bindir}/jvisualvm jvisualvm %{prefix}/bin/jvisualvm \
  --slave %{_bindir}/native2ascii native2ascii %{prefix}/bin/native2ascii \
  --slave %{_bindir}/rmic rmic %{prefix}/bin/rmic \
  --slave %{_bindir}/schemagen schemagen %{prefix}/bin/schemagen \
  --slave %{_bindir}/serialver serialver %{prefix}/bin/serialver \
  --slave %{_bindir}/wsgen wsgen %{prefix}/bin/wsgen \
  --slave %{_bindir}/wsimport wsimport %{prefix}/bin/wsimport \
  --slave %{_bindir}/xjc xjc %{prefix}/bin/xjc \
  --slave %{_mandir}/man1/appletviewer.1 appletviewer.1 %{prefix}/man/man1/appletviewer.1 \
  --slave %{_mandir}/man1/apt.1 apt.1 %{prefix}/man/man1/apt.1 \
  --slave %{_mandir}/man1/extcheck.1 extcheck.1 %{prefix}/man/man1/extcheck.1 \
  --slave %{_mandir}/man1/idlj.1 idlj.1 %{prefix}/man/man1/idlj.1 \
  --slave %{_mandir}/man1/jar.1 jar.1 %{prefix}/man/man1/jar.1 \
  --slave %{_mandir}/man1/jarsigner.1 jarsigner.1 %{prefix}/man/man1/jarsigner.1 \
  --slave %{_mandir}/man1/javac.1 javac.1 %{prefix}/man/man1/javac.1 \
  --slave %{_mandir}/man1/javadoc.1 javadoc.1 %{prefix}/man/man1/javadoc.1 \
  --slave %{_mandir}/man1/javah.1 javah.1 %{prefix}/man/man1/javah.1 \
  --slave %{_mandir}/man1/javap.1 javap.1 %{prefix}/man/man1/javap.1 \
  --slave %{_mandir}/man1/jconsole.1 jconsole.1 %{prefix}/man/man1/jconsole.1 \
  --slave %{_mandir}/man1/jdb.1 jdb.1 %{prefix}/man/man1/jdb.1 \
  --slave %{_mandir}/man1/jhat.1 jhat.1 %{prefix}/man/man1/jhat.1 \
  --slave %{_mandir}/man1/jinfo.1 jinfo.1 %{prefix}/man/man1/jinfo.1 \
  --slave %{_mandir}/man1/jmap.1 jmap.1 %{prefix}/man/man1/jmap.1 \
  --slave %{_mandir}/man1/jps.1 jps.1 %{prefix}/man/man1/jps.1 \
  --slave %{_mandir}/man1/jrunscript.1 jrunscript.1 %{prefix}/man/man1/jrunscript.1 \
  --slave %{_mandir}/man1/jsadebugd.1 jsadebugd.1 %{prefix}/man/man1/jsadebugd.1 \
  --slave %{_mandir}/man1/jstack.1 jstack.1 %{prefix}/man/man1/jstack.1 \
  --slave %{_mandir}/man1/jstat.1 jstat.1 %{prefix}/man/man1/jstat.1 \
  --slave %{_mandir}/man1/jstatd.1 jstatd.1 %{prefix}/man/man1/jstatd.1 \
  --slave %{_mandir}/man1/jvisualvm.1 jvisualvm.1 %{prefix}/man/man1/jvisualvm.1 \
  --slave %{_mandir}/man1/native2ascii.1 native2ascii.1 %{prefix}/man/man1/native2ascii.1 \
  --slave %{_mandir}/man1/rmic.1 rmic.1 %{prefix}/man/man1/rmic.1 \
  --slave %{_mandir}/man1/schemagen.1 schemagen.1 %{prefix}/man/man1/schemagen.1 \
  --slave %{_mandir}/man1/serialver.1 serialver.1 %{prefix}/man/man1/serialver.1 \
  --slave %{_mandir}/man1/wsgen.1 wsgen.1 %{prefix}/man/man1/wsgen.1 \
  --slave %{_mandir}/man1/wsimport.1 wsimport.1 %{prefix}/man/man1/wsimport.1 \
  --slave %{_mandir}/man1/xjc.1 xjc.1 %{prefix}/man/man1/xjc.1
 
%postun 
if [ $1 -eq 0 ]
then
  alternatives --remove java %{prefix}/bin/java
  alternatives --remove javac %{prefix}/bin/javac
fi
