%bcond_with tests
%bcond_without python2

Summary:	Python library for determining image sizes

Name:		python-imagesize
Version:	1.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/41/f5/3cf63735d54aa9974e544aa25858d8f9670ac5b4da51020bbfc6aaade741/imagesize-1.1.0.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/imagesize
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
BuildRequires:	python3-distribute
BuildRequires:	pkgconfig(python3)
BuildRequires:	python2-setuptools
BuildRequires:	python2-pkg-resources

%description
Python library for determining image sizes

%if %{with python2}
%package -n python2-imagesize
Summary:	Python library for determining image sizes
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools

%description -n python2-imagesize
Python library for determining image sizes
%endif

%prep
%setup -qc -b 0
mv imagesize-%{version} python3

%if %{with python2}
cp -r python3 python2
%endif

%build
%if %{with python2}
cd python2
python2 setup.py build
cd ..
%endif

cd python3
python setup.py build
cd ..

%install
%if %{with python2}
cd python2
python2 setup.py install --skip-build --root %{buildroot}
cd ..
%endif

cd python3
python setup.py install --skip-build --root=%{buildroot} 
cd ..

%check
%if %{with tests}
%if %{with python2}
cd python2/tests
python2 run.py
cd ../..
%endif
cd python3
make test
cd ..
%endif

%files
%{py_puresitedir}/*

%if %{with python2}
%files -n python2-imagesize
%{py2_puresitedir}/*
%endif
