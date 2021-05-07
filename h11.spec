#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : h11
Version  : 0.12.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/bd/e9/72c3dc8f7dd7874812be6a6ec788ba1300bfe31570963a7e788c86280cb9/h11-0.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/bd/e9/72c3dc8f7dd7874812be6a6ec788ba1300bfe31570963a7e788c86280cb9/h11-0.12.0.tar.gz
Summary  : A pure-Python, bring-your-own-I/O implementation of HTTP/1.1
Group    : Development/Tools
License  : MIT
Requires: h11-license = %{version}-%{release}
Requires: h11-python = %{version}-%{release}
Requires: h11-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===

%package license
Summary: license components for the h11 package.
Group: Default

%description license
license components for the h11 package.


%package python
Summary: python components for the h11 package.
Group: Default
Requires: h11-python3 = %{version}-%{release}

%description python
python components for the h11 package.


%package python3
Summary: python3 components for the h11 package.
Group: Default
Requires: python3-core
Provides: pypi(h11)

%description python3
python3 components for the h11 package.


%prep
%setup -q -n h11-0.12.0
cd %{_builddir}/h11-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609775992
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/h11
cp %{_builddir}/h11-0.12.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/h11/538b04fc7835aa9ba3e5de009b5324007eb5a3d2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/h11/538b04fc7835aa9ba3e5de009b5324007eb5a3d2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
