Name:		texlive-clearsans
Version:	64400
Release:	1
Summary:	Clear Sans fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/clearsans
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clearsans.r64400.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clearsans.doc.r64400.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Clear Sans was designed by Daniel Ratighan at Monotype under
the direction of the User Experience team at Intel's Open
Source Technology Center. Clear Sans is available in three
weights (regular, medium, and bold) with corresponding italics,
plus light and thin upright (without italics). Clear Sans has
minimized, unambiguous characters and slightly narrow
proportions, making it ideal for UI design. Its strong,
recognizable forms avoid distracting ambiguity, making Clear
Sans comfortable for reading short UI labels and long passages
in both screen and print. The fonts are available in both
TrueType and Type 1 formats.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/clearsans
%{_texmfdistdir}/fonts/map/dvips/clearsans
%{_texmfdistdir}/fonts/tfm/intel/clearsans
%{_texmfdistdir}/fonts/truetype/intel/clearsans
%{_texmfdistdir}/fonts/type1/intel/clearsans
%{_texmfdistdir}/fonts/vf/intel/clearsans
%{_texmfdistdir}/tex/latex/clearsans
%doc %{_texmfdistdir}/doc/fonts/clearsans

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
