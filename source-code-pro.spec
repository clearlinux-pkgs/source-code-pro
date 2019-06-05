#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : source-code-pro
Version  : 1.050r.it
Release  : 4
URL      : https://github.com/adobe-fonts/source-code-pro/archive/2.030R-ro/1.050R-it.tar.gz
Source0  : https://github.com/adobe-fonts/source-code-pro/archive/2.030R-ro/1.050R-it.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.1
Requires: source-code-pro-data
Patch1: 0001-makefile.patch

%description
# Source Code Pro
Source Code Pro is a set of OpenType fonts that have been designed to work well
in user interface (UI) environments. In addition to a functional OpenType font, this open
source project provides all of the source files that were used to build this OpenType font
by using the AFDKO makeotf tool.

%package data
Summary: data components for the source-code-pro package.
Group: Data

%description data
data components for the source-code-pro package.


%prep
%setup -q -n source-code-pro-2.030R-ro-1.050R-it
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509473372
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1509473372
rm -rf %{buildroot}
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
