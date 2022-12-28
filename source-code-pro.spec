#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : source-code-pro
Version  : 1.017r
Release  : 6
URL      : https://github.com/adobe-fonts/source-code-pro/archive/1.017R/source-code-pro-1.017R.tar.gz
Source0  : https://github.com/adobe-fonts/source-code-pro/archive/1.017R/source-code-pro-1.017R.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.1
Requires: source-code-pro-data = %{version}-%{release}
Requires: source-code-pro-license = %{version}-%{release}
Patch1: 0001-makefile.patch

%description
<!DOCTYPE html>
<html>
<head>
<title>Read Me File for Adobe® OpenType® Fonts</title>
<meta charset="utf-8" />
</head>
<body bgcolor="white" link="#ce0000" alink="#ce0000" vlink="#9c6363">
<h2><font color="#333333"
face="verdana,geneva,arial">Adobe&reg; OpenType&reg; Fonts</font></h2>
<p><font size="2" face="verdana,geneva,arial">Thank
you for licensing Adobe OpenType fonts. In order to ensure that you
have the most up-to-date product information, Adobe has posted <a
href="http://www.adobe.com/type/browser/OTReadMe.html">an OpenType
Read Me file</a> on the Adobe web site that contains information such
as minimum system requirements, technical support contact information
and software installation notes. We have also posted <a
href="http://www.adobe.com/type/browser/pdfs/OTGuide.pdf">an OpenType
User's Guide</a> in PDF format on the Adobe web site that can be
viewed online and downloaded to your computer. <P>If you have
licensed an Adobe OpenType Pro font, there may be additional PDF
documents, such as a specimen book, a glyph complement showing, and a
typeface-specific Read Me file, available on the typeface&#146;s
product pages on the Adobe web site. These additional files may be
viewed online or downloaded to your computer.<P>To get you started
quickly, below are links to localized installation instructions for
your fonts.

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
%setup -q -n source-code-pro-1.017R
cd %{_builddir}/source-code-pro-1.017R
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672201633
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1672201633
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/source-code-pro
cp %{_builddir}/source-code-pro-1.017R/LICENSE.txt %{buildroot}/usr/share/package-licenses/source-code-pro/689c1517e0db480765a3c35f13a7d942779d7e5e
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Black.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Bold.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-ExtraLight.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Light.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Medium.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf
/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Semibold.otf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/source-code-pro/689c1517e0db480765a3c35f13a7d942779d7e5e
