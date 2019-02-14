RPM_NAME=oracle-jdk8-qhr
RPM_JDK_UPDATE=202
RPM_VERSION="1.8.0_${RPM_JDK_UPDATE}"
RPM_RELEASE=1
RPM_ARCH=x86_64

# End of Configurable Settings

RPM_FILE_PREFIX=${RPM_NAME}-${RPM_VERSION}-${RPM_RELEASE}
SRPM_FILE=${RPM_FILE_PREFIX}.src.rpm
RPM_FILE=${RPM_FILE_PREFIX}.${RPM_ARCH}.rpm

SPEC_FILE=jdk8.spec

BUILD_DEFINES=--define "name ${RPM_NAME}" --define "version ${RPM_VERSION}" --define "release ${RPM_RELEASE}" --define "jdk_update ${RPM_JDK_UPDATE}"


MOCKOUTPUTFILES=build.log hw_info.log installed_pkgs.log root.log state.log
SOURCES=sources/jdk-8u${RPM_JDK_UPDATE}-linux-x64.tar.gz

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

sources/jdk-8u${RPM_JDK_UPDATE}-linux-x64.tar.gz:
	wget --progress=dot:mega -O "$@" --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u${RPM_JDK_UPDATE}-b08/1961070e4c9b4e26a04e7f5a083f551e/jdk-8u${RPM_JDK_UPDATE}-linux-x64.tar.gz
