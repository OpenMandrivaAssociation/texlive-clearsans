# revision 33207
# category Package
# catalog-ctan /fonts/clearsans
# catalog-date 2014-04-09 15:04:56 +0200
# catalog-license apache2
# catalog-version undef
Name:		texlive-clearsans
Version:	20140409
Release:	4
Summary:	Clear Sans fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/clearsans
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clearsans.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clearsans.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/clearsans/clr_er7w2x.enc
%{_texmfdistdir}/fonts/enc/dvips/clearsans/clr_nrghxx.enc
%{_texmfdistdir}/fonts/enc/dvips/clearsans/clr_y7ge35.enc
%{_texmfdistdir}/fonts/enc/dvips/clearsans/clr_zjpm5y.enc
%{_texmfdistdir}/fonts/map/dvips/clearsans/ClearSans.map
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Light-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Light-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Light-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Light-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Light-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Light-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Light-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Medium-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Medium-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Medium-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Medium-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Medium-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Medium-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Medium-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-MediumItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-MediumItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-MediumItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-MediumItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-MediumItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-MediumItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-MediumItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Thin-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Thin-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Thin-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Thin-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Thin-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Thin-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-Thin-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/intel/clearsans/ClearSans-lf-ts1.tfm
%{_texmfdistdir}/fonts/truetype/intel/clearsans/ClearSans-Bold.ttf
%{_texmfdistdir}/fonts/truetype/intel/clearsans/ClearSans-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/intel/clearsans/ClearSans-Italic.ttf
%{_texmfdistdir}/fonts/truetype/intel/clearsans/ClearSans-Light.ttf
%{_texmfdistdir}/fonts/truetype/intel/clearsans/ClearSans-Medium.ttf
%{_texmfdistdir}/fonts/truetype/intel/clearsans/ClearSans-MediumItalic.ttf
%{_texmfdistdir}/fonts/truetype/intel/clearsans/ClearSans-Regular.ttf
%{_texmfdistdir}/fonts/truetype/intel/clearsans/ClearSans-Thin.ttf
%{_texmfdistdir}/fonts/type1/intel/clearsans/ClearSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/intel/clearsans/ClearSans-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/intel/clearsans/ClearSans-Italic.pfb
%{_texmfdistdir}/fonts/type1/intel/clearsans/ClearSans-Light.pfb
%{_texmfdistdir}/fonts/type1/intel/clearsans/ClearSans-Medium.pfb
%{_texmfdistdir}/fonts/type1/intel/clearsans/ClearSans-MediumItalic.pfb
%{_texmfdistdir}/fonts/type1/intel/clearsans/ClearSans-Regular.pfb
%{_texmfdistdir}/fonts/type1/intel/clearsans/ClearSans-Thin.pfb
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Light-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Light-lf-t1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Light-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Medium-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Medium-lf-t1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Medium-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-MediumItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-MediumItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-MediumItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Thin-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Thin-lf-t1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-Thin-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-lf-t1.vf
%{_texmfdistdir}/fonts/vf/intel/clearsans/ClearSans-lf-ts1.vf
%{_texmfdistdir}/tex/latex/clearsans/ClearSans.sty
%{_texmfdistdir}/tex/latex/clearsans/LY1ClearSans-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/LY1ClearSansLight-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/LY1ClearSansThin-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/OT1ClearSans-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/OT1ClearSansLight-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/OT1ClearSansThin-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/T1ClearSans-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/T1ClearSansLight-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/T1ClearSansThin-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/TS1ClearSans-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/TS1ClearSansLight-LF.fd
%{_texmfdistdir}/tex/latex/clearsans/TS1ClearSansThin-LF.fd
%doc %{_texmfdistdir}/doc/fonts/clearsans/LICENSE-2.0.txt
%doc %{_texmfdistdir}/doc/fonts/clearsans/README
%doc %{_texmfdistdir}/doc/fonts/clearsans/clear-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/clearsans/clear-samples.tex
%doc %{_texmfdistdir}/doc/fonts/clearsans/clearsans.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
