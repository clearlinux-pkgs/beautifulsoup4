#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : beautifulsoup4
Version  : 4.9.1
Release  : 65
URL      : https://files.pythonhosted.org/packages/c6/62/8a2bef01214eeaa5a4489eca7104e152968729512ee33cb5fbbc37a896b7/beautifulsoup4-4.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c6/62/8a2bef01214eeaa5a4489eca7104e152968729512ee33cb5fbbc37a896b7/beautifulsoup4-4.9.1.tar.gz
Summary  : Screen-scraping library
Group    : Development/Tools
License  : MIT
Requires: beautifulsoup4-license = %{version}-%{release}
Requires: beautifulsoup4-python = %{version}-%{release}
Requires: beautifulsoup4-python3 = %{version}-%{release}
Requires: html5lib
Requires: lxml
Requires: soupsieve
BuildRequires : buildreq-distutils3
BuildRequires : html5lib
BuildRequires : lxml
BuildRequires : py
BuildRequires : pytest
BuildRequires : soupsieve

%description
Beautiful Soup is a Python package for parsing HTML and XML documents.

%package license
Summary: license components for the beautifulsoup4 package.
Group: Default

%description license
license components for the beautifulsoup4 package.


%package python
Summary: python components for the beautifulsoup4 package.
Group: Default
Requires: beautifulsoup4-python3 = %{version}-%{release}

%description python
python components for the beautifulsoup4 package.


%package python3
Summary: python3 components for the beautifulsoup4 package.
Group: Default
Requires: python3-core
Provides: pypi(beautifulsoup4)
Requires: pypi(soupsieve)

%description python3
python3 components for the beautifulsoup4 package.


%prep
%setup -q -n beautifulsoup4-4.9.1
cd %{_builddir}/beautifulsoup4-4.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589951424
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/beautifulsoup4
cp %{_builddir}/beautifulsoup4-4.9.1/COPYING.txt %{buildroot}/usr/share/package-licenses/beautifulsoup4/96063bf55c010062c01e3792177b9fabda28eb82
cp %{_builddir}/beautifulsoup4-4.9.1/LICENSE %{buildroot}/usr/share/package-licenses/beautifulsoup4/1295b7c053fbc5d5bfe3b7aac318703d01d1e227
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/beautifulsoup4/1295b7c053fbc5d5bfe3b7aac318703d01d1e227
/usr/share/package-licenses/beautifulsoup4/96063bf55c010062c01e3792177b9fabda28eb82

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
