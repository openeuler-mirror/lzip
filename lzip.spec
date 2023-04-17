Name:           lzip
Version:        1.20
Release:        3
Summary:        LZMA compressor with integrity checking

License:        GPLv3+
URL:            http://www.nongnu.org/lzip/lzip.html
Source0:        http://download.savannah.gnu.org/releases/lzip/lzip-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
Lzip compresses data using LZMA (Lempel-Ziv-Markov chain-Algorithm). It
supports integrity checking using CRC (Cyclic Redundancy Check). To archive
multiple files, tar can be used with lzip. Please note, that the lzip file
format (.lz) is not compatible with the lzma file format (.lzma).


%prep
%setup -q
# file needs to be copied, because it is used in "make check"
cp -a COPYING{,.txt}
# convert CRLF to LF
sed -i 's/\r//' COPYING.txt 


%build
%configure CXX=$CXX CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}"
make %{?_smp_mflags}


%install
make install install-man DESTDIR=$RPM_BUILD_ROOT

# if install-info is present, this is created by upstream's makefile
rm -Rf $RPM_BUILD_ROOT%{_infodir}/dir

%check
make check

%files
%license COPYING.txt
# TODO is currently empty
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/lzip
%{_infodir}/lzip.info*
%{_mandir}/man1/lzip.1*


%changelog
* Mon Apr 17 2023 Xiaoya Huang <huangxiaoya@iscas.ac.cn> - 1.20-3
- Support specify compiler

* Tue Dec 14 2021 konglidong <konglidong@uniontech.com> - 1.20-2
- delete %dist

* Tue May 05 2020 Hubble Zhu <zhuhengbo1@huawei.com> - 1.20-1
- First release.
