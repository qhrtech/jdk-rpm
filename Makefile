RPM_NAME=oracle-jdk9-qhr
RPM_JDK_UPDATE=4
RPM_VERSION="9.0.${RPM_JDK_UPDATE}"
RPM_RELEASE=1
RPM_ARCH=x86_64

# End of Configurable Settings


RPM_FILE_PREFIX=${RPM_NAME}-${RPM_VERSION}-${RPM_RELEASE}
SRPM_FILE=${RPM_FILE_PREFIX}.src.rpm
RPM_FILE=${RPM_FILE_PREFIX}.${RPM_ARCH}.rpm

SPEC_FILE=jdk.spec

BUILD_DEFINES=--define "name ${RPM_NAME}" --define "version ${RPM_VERSION}" --define "release ${RPM_RELEASE}" --define "jdk_update ${RPM_JDK_UPDATE}"


MOCKOUTPUTFILES=build.log hw_info.log installed_pkgs.log root.log state.log
SOURCES=sources/jdk-9.0.${RPM_JDK_UPDATE}_linux-x64_bin.tar.gz

default: ${RPM_FILE}

${SRPM_FILE}: sources ${SPEC_FILE}
	rpmbuild --define "_sourcedir ${PWD}/sources" --define "_srcrpmdir ${PWD}" ${BUILD_DEFINES} -bs ${SPEC_FILE}

${RPM_FILE}: ${SRPM_FILE}
	mock -r rhel-7-x86_64 ${BUILD_DEFINES} "--resultdir=${PWD}" ${SRPM_FILE}

clean:
	rm -fr *.rpm $(MOCKOUTPUTFILES) sources


sources: sources-dir $(SOURCES) sources-checksum

sources-dir:
	mkdir -p sources

sources-checksum:
	sha512sum --check sources-sha512sums

sources-update-checksum:
	sha512sum $(SOURCES) > sources-sha512sums
	

sources/jdk-9.0.${RPM_JDK_UPDATE}_linux-x64_bin.tar.gz:
	wget -O "$@" --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/9.0.4+11/c2514751926b4512b076cc82f959763f/jdk-9.0.4_linux-x64_bin.tar.gz
