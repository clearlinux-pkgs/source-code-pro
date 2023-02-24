#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : source-code-pro
Version  : 2.038r.ro1.058r.it1.018r.var
Release  : 7
URL      : https://github.com/adobe-fonts/source-code-pro/releases/download/2.038R-ro%2F1.058R-it%2F1.018R-VAR/OTF-source-code-pro-2.038R-ro-1.058R-it.zip
Source0  : https://github.com/adobe-fonts/source-code-pro/releases/download/2.038R-ro%2F1.058R-it%2F1.018R-VAR/OTF-source-code-pro-2.038R-ro-1.058R-it.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.1
Requires: source-code-pro-data = %{version}-%{release}
Requires: source-code-pro-license = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-makefile.patch

%description
No detailed description available

%package data
Summary: data components for the source-code-pro package.
Group: Data

%description data
data components for the source-code-pro package.


%package license
Summary: license components for the source-code-pro package.
Group: Default

%description license
license components for the source-code-pro package.


%prep
%setup -q -c -n OTF-source-code-pro-2.038R-ro-1.058R-it
cd %{_builddir}/OTF-source-code-pro-2.038R-ro-1.058R-it
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677198079
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1677198079
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/source-code-pro
cp %{_builddir}/OTF-source-code-pro-2.038R-ro-1.058R-it/LICENSE.md %{buildroot}/usr/share/package-licenses/source-code-pro/aadfb3c7e823099ad89080c398362bebb9ecc161 || :
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Black.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-BlackIt.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Bold.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-BoldIt.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-ExtraLight.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-ExtraLightIt.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-It.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Light.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-LightIt.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Medium.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-MediumIt.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Semibold.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-SemiboldIt.otf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/source-code-pro/aadfb3c7e823099ad89080c398362bebb9ecc161
