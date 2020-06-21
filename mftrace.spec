Summary:	Generate scalable fonts for TeX
Summary(pl.UTF-8):	Generowanie skalowanych fontów dla TeXa
Name:		mftrace
Version:	1.2.13
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	https://lilypond.org/download/sources/mftrace/%{name}-%{version}.tar.gz
# Source0-md5:	0d3f2ae9cff1f2677fbf968eb40c9238
URL:		http://lilypond.org/mftrace/
Requires:	potrace
Requires:	python >= 2.1
Requires:	t1utils
Requires:	tetex-metafont
Conflicts:	autotrace < 0.30
Conflicts:	pfaedit < 020215
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mftrace is a small Python program that lets you trace a TeX bitmap
font into a PFA or PFB font (A PostScript Type1 Scalable Font). It is
licensed under the GNU GPL.

Type1 fonts offer many advantages over bitmaps, as they allow
PostScript files to render correctly on printers with many
resolutions. Moreover, Ghostscript can generate much better PDF, if
given scalable fonts.

Note: fontforge (or pfaedit >= 020215) is recommended for autohinting.

%description -l pl.UTF-8
mftrace to mały program w Pythonie pozwalający na trasowanie TeXowych
fontów bitmapowych do fontów PFA lub PFB (skalowanych fontów
PostScript Type1). Program jest rozpowszechniany na licencji GNU GPL.

Fonty Type1 oferują wiele zalet w stosunku do bitmap, jako że
pozwalają na poprawne odwzorowanie plików w PostScripcie na drukarkach
w wielu rozdzielczościach. Co więcej, ghostscript może generować dużo
lepsze PDF-y, jeśli ma skalowalne fonty.

Zalecany jest pakiet fontforge (lub pfaedit >= 020215) do
automatycznego hintingu.

%prep
%setup -q

%build
%configure \
	POTRACE=/usr/bin/potrace \
	PYTHON=%{__python} \
	AUTOTRACE=/usr/bin/autotrace

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL=install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt
%attr(755,root,root) %{_bindir}/gf2pbm
%attr(755,root,root) %{_bindir}/mftrace
%{_mandir}/man1/mftrace.1*
%dir %{_datadir}/mftrace
%{_datadir}/mftrace/afm.pyc
%{_datadir}/mftrace/afm.py
%{_datadir}/mftrace/tfm.pyc
%{_datadir}/mftrace/tfm.py
