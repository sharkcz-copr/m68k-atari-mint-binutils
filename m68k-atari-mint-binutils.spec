%global patchdate 20180703

Summary:        MiNT binutils
Name:           m68k-atari-mint-binutils
Version:        2.30
Release:        1%{?dist}
License:        GPLv2+ and LGPLv2+ and GPLv3+ and LGPLv3+
URL:            https://www.gnu.org/software/binutils/
Source0:        https://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.bz2
Patch0:         http://vincent.riviere.free.fr/soft/m68k-atari-mint/archives/binutils-%{version}-mint-%{patchdate}.patch.bz2
BuildRequires:  m68k-atari-mint-filesystem
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  autoconf automake
BuildRequires:  make

Requires:       m68k-atari-mint-filesystem
Requires:       m68k-atari-mint-mintbin


%description
Binutils is a collection of utilities necessary for compiling programs. It
includes the assembler and linker, as well as a number of other
miscellaneous programs for dealing with executable formats.


%prep
%setup -q -n binutils-%{version}
%patch0 -p1 -b .mint


%build
mkdir build
pushd build

CFLAGS="%build_cflags -Wno-unused-const-variable" \
LDFLAGS="%build_ldflags " \
../configure \
  --build=%_build --host=%_host \
  --target=%{mint_target} \
  --disable-nls \
  --with-sysroot=%{mint_sysroot} \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir}

%make_build
popd


%install
pushd build
%make_install
popd

# These files conflict with ordinary binutils.
rm -rf %{buildroot}%{_infodir}
rm -f %{buildroot}%{_libdir}/libiberty*

# Remove unwanted files
rm %{buildroot}%{_bindir}/%{mint_target}-readelf*
rm %{buildroot}%{_mandir}/man1/%{mint_target}-readelf.1*
rm %{buildroot}%{_mandir}/man1/%{mint_target}-dlltool.1*
rm %{buildroot}%{_mandir}/man1/%{mint_target}-nlmconv.1*
rm %{buildroot}%{_mandir}/man1/%{mint_target}-windmc.1*
rm %{buildroot}%{_mandir}/man1/%{mint_target}-windres.1*


%files
%doc README
%{_bindir}/%{mint_target}-*
%{_mandir}/man1/%{mint_target}-*
%{_prefix}/%{mint_target}/bin/*
%{_prefix}/%{mint_target}/lib/ldscripts


%changelog
* Mon Jun 13 2022 Dan Horák <dan[at]danny.cz> - 2.30-1
- updated to 2.30 with 20180703

* Sat May 10 2014 Dan Horák <dan[at]danny.cz> - 2.24-2
- fix build with gcc 4.9

* Fri May 09 2014 Dan Horák <dan[at]danny.cz> - 2.24-1
- updated to 2.24

* Sat Jan 05 2013 Dan Horák <dan[at]danny.cz> - 2.23.1-1
- updated to 2.23.1

* Sun Mar 25 2012 Dan Horák <dan[at]danny.cz> - 2.22-1
- updated to 2.22
- spec cleanup

* Wed Aug 03 2011 Dan Horák <dan[at]danny.cz> - 2.21.1-1
- initial Fedora release
