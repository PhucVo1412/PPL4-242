# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u027d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0080\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u008a\n\5\3\6\3\6")
        buf.write("\3\6\3\6\5\6\u0090\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\5\b\u009f\n\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00a6\n\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00ae\n\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00b7\n\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c2\n\r\3\16\3\16\3")
        buf.write("\16\5\16\u00c7\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00d0\n\17\3\20\3\20\3\20\3\21\3\21\5\21\u00d7\n")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u00dd\n\21\3\21\5\21\u00e0")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00e8\n\22\f")
        buf.write("\22\16\22\u00eb\13\22\3\23\3\23\3\23\3\23\3\23\3\23\7")
        buf.write("\23\u00f3\n\23\f\23\16\23\u00f6\13\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\7\24\u00fe\n\24\f\24\16\24\u0101\13\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\7\25\u0109\n\25\f\25\16\25")
        buf.write("\u010c\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0114")
        buf.write("\n\26\f\26\16\26\u0117\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u011e\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0130")
        buf.write("\n\30\3\30\7\30\u0133\n\30\f\30\16\30\u0136\13\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0144\n\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u0152\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\7\34\u015c\n\34\f\34\16\34\u015f")
        buf.write("\13\34\3\35\3\35\5\35\u0163\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u016a\n\36\3\37\3\37\3\37\3\37\5\37\u0170\n\37")
        buf.write("\3 \3 \3 \5 \u0175\n \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u0187\n \3!\3!\3!\3!\3!\5!\u018e\n")
        buf.write("!\3!\3!\5!\u0192\n!\3!\3!\3!\5!\u0197\n!\3!\3!\3!\3\"")
        buf.write("\3\"\5\"\u019e\n\"\3#\3#\3#\3#\3#\3#\3#\5#\u01a7\n#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01ba")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01c5\n&\3&\3&\5&\u01c9")
        buf.write("\n&\3&\3&\3&\5&\u01ce\n&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3(\3(\5(\u01e0\n(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\5(\u01ea\n(\3(\3(\5(\u01ee\n(\3)\3)\5)\u01f2")
        buf.write("\n)\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01fc\n*\3+\3+\3+\3+\5")
        buf.write("+\u0202\n+\3,\3,\3,\3,\3,\5,\u0209\n,\3,\3,\3,\3,\5,\u020f")
        buf.write("\n,\3,\3,\3,\5,\u0214\n,\3-\3-\3-\3-\3.\3.\3.\5.\u021d")
        buf.write("\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0228\n/\3/\5/\u022b")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u0237\n\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u0243\n\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\5\63\u0252\n")
        buf.write("\63\3\63\3\63\5\63\u0256\n\63\3\63\3\63\5\63\u025a\n\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u0263\n\63\3")
        buf.write("\64\3\64\3\64\3\64\3\65\3\65\3\65\5\65\u026c\n\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\58\u0277\n8\39\3")
        buf.write("9\59\u027b\n9\39\2\t\"$&(*.\66:\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnp\2\n\5\2\24\26\679;;\4\2\13\16\67\67\3\2")
        buf.write("\678\3\2\34!\3\2\27\30\3\2\31\33\4\2%%\'+\4\2--\67\67")
        buf.write("\2\u029a\2r\3\2\2\2\4u\3\2\2\2\6\177\3\2\2\2\b\u0089\3")
        buf.write("\2\2\2\n\u008f\3\2\2\2\f\u0091\3\2\2\2\16\u009e\3\2\2")
        buf.write("\2\20\u00a5\3\2\2\2\22\u00ad\3\2\2\2\24\u00af\3\2\2\2")
        buf.write("\26\u00b6\3\2\2\2\30\u00c1\3\2\2\2\32\u00c3\3\2\2\2\34")
        buf.write("\u00cf\3\2\2\2\36\u00d1\3\2\2\2 \u00df\3\2\2\2\"\u00e1")
        buf.write("\3\2\2\2$\u00ec\3\2\2\2&\u00f7\3\2\2\2(\u0102\3\2\2\2")
        buf.write("*\u010d\3\2\2\2,\u011d\3\2\2\2.\u011f\3\2\2\2\60\u0143")
        buf.write("\3\2\2\2\62\u0145\3\2\2\2\64\u0151\3\2\2\2\66\u0153\3")
        buf.write("\2\2\28\u0162\3\2\2\2:\u0169\3\2\2\2<\u016f\3\2\2\2>\u0186")
        buf.write("\3\2\2\2@\u0188\3\2\2\2B\u019d\3\2\2\2D\u01a6\3\2\2\2")
        buf.write("F\u01a8\3\2\2\2H\u01b9\3\2\2\2J\u01bb\3\2\2\2L\u01d2\3")
        buf.write("\2\2\2N\u01ed\3\2\2\2P\u01f1\3\2\2\2R\u01fb\3\2\2\2T\u0201")
        buf.write("\3\2\2\2V\u0213\3\2\2\2X\u0215\3\2\2\2Z\u021c\3\2\2\2")
        buf.write("\\\u021e\3\2\2\2^\u0242\3\2\2\2`\u0244\3\2\2\2b\u0249")
        buf.write("\3\2\2\2d\u0262\3\2\2\2f\u0264\3\2\2\2h\u0268\3\2\2\2")
        buf.write("j\u0270\3\2\2\2l\u0272\3\2\2\2n\u0276\3\2\2\2p\u0278\3")
        buf.write("\2\2\2rs\5<\37\2st\7\2\2\3t\3\3\2\2\2uv\t\2\2\2v\5\3\2")
        buf.write("\2\2w\u0080\78\2\2x\u0080\79\2\2y\u0080\7;\2\2z\u0080")
        buf.write("\7\25\2\2{\u0080\7\26\2\2|\u0080\7\24\2\2}\u0080\5\f\7")
        buf.write("\2~\u0080\5\24\13\2\177w\3\2\2\2\177x\3\2\2\2\177y\3\2")
        buf.write("\2\2\177z\3\2\2\2\177{\3\2\2\2\177|\3\2\2\2\177}\3\2\2")
        buf.write("\2\177~\3\2\2\2\u0080\7\3\2\2\2\u0081\u0082\5\16\b\2\u0082")
        buf.write("\u0083\5\b\5\2\u0083\u008a\3\2\2\2\u0084\u008a\7\f\2\2")
        buf.write("\u0085\u008a\7\13\2\2\u0086\u008a\7\r\2\2\u0087\u008a")
        buf.write("\7\16\2\2\u0088\u008a\7\67\2\2\u0089\u0081\3\2\2\2\u0089")
        buf.write("\u0084\3\2\2\2\u0089\u0085\3\2\2\2\u0089\u0086\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\t\3\2\2")
        buf.write("\2\u008b\u008c\7\67\2\2\u008c\u008d\7\64\2\2\u008d\u0090")
        buf.write("\5\n\6\2\u008e\u0090\7\67\2\2\u008f\u008b\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\13\3\2\2\2\u0091\u0092\5\16\b\2\u0092")
        buf.write("\u0093\t\3\2\2\u0093\u0094\7\60\2\2\u0094\u0095\5\20\t")
        buf.write("\2\u0095\u0096\7\61\2\2\u0096\r\3\2\2\2\u0097\u0098\7")
        buf.write("\62\2\2\u0098\u0099\t\4\2\2\u0099\u009a\7\63\2\2\u009a")
        buf.write("\u009f\5\16\b\2\u009b\u009c\7\62\2\2\u009c\u009d\t\4\2")
        buf.write("\2\u009d\u009f\7\63\2\2\u009e\u0097\3\2\2\2\u009e\u009b")
        buf.write("\3\2\2\2\u009f\17\3\2\2\2\u00a0\u00a1\5\22\n\2\u00a1\u00a2")
        buf.write("\7\64\2\2\u00a2\u00a3\5\20\t\2\u00a3\u00a6\3\2\2\2\u00a4")
        buf.write("\u00a6\5\22\n\2\u00a5\u00a0\3\2\2\2\u00a5\u00a4\3\2\2")
        buf.write("\2\u00a6\21\3\2\2\2\u00a7\u00ae\5\4\3\2\u00a8\u00ae\5")
        buf.write("\24\13\2\u00a9\u00aa\7\60\2\2\u00aa\u00ab\5\20\t\2\u00ab")
        buf.write("\u00ac\7\61\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00a7\3\2\2")
        buf.write("\2\u00ad\u00a8\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ae\23\3")
        buf.write("\2\2\2\u00af\u00b0\7\67\2\2\u00b0\u00b1\7\60\2\2\u00b1")
        buf.write("\u00b2\5\26\f\2\u00b2\u00b3\7\61\2\2\u00b3\25\3\2\2\2")
        buf.write("\u00b4\u00b7\5\30\r\2\u00b5\u00b7\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\27\3\2\2\2\u00b8\u00b9")
        buf.write("\7\67\2\2\u00b9\u00ba\7\66\2\2\u00ba\u00bb\5\"\22\2\u00bb")
        buf.write("\u00bc\7\64\2\2\u00bc\u00bd\5\30\r\2\u00bd\u00c2\3\2\2")
        buf.write("\2\u00be\u00bf\7\67\2\2\u00bf\u00c0\7\66\2\2\u00c0\u00c2")
        buf.write("\5\"\22\2\u00c1\u00b8\3\2\2\2\u00c1\u00be\3\2\2\2\u00c2")
        buf.write("\31\3\2\2\2\u00c3\u00c4\7\67\2\2\u00c4\u00c6\7.\2\2\u00c5")
        buf.write("\u00c7\5\34\17\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7\3\2\2")
        buf.write("\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\7/\2\2\u00c9\33\3\2")
        buf.write("\2\2\u00ca\u00cb\5\"\22\2\u00cb\u00cc\7\64\2\2\u00cc\u00cd")
        buf.write("\5\34\17\2\u00cd\u00d0\3\2\2\2\u00ce\u00d0\5\"\22\2\u00cf")
        buf.write("\u00ca\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\35\3\2\2\2\u00d1")
        buf.write("\u00d2\5 \21\2\u00d2\u00d3\5\32\16\2\u00d3\37\3\2\2\2")
        buf.write("\u00d4\u00d7\7\67\2\2\u00d5\u00d7\5\62\32\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d9\7,\2\2\u00d9\u00e0\5 \21\2\u00da\u00dd\7\67\2\2")
        buf.write("\u00db\u00dd\5\62\32\2\u00dc\u00da\3\2\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0\7,\2\2\u00df")
        buf.write("\u00d6\3\2\2\2\u00df\u00dc\3\2\2\2\u00e0!\3\2\2\2\u00e1")
        buf.write("\u00e2\b\22\1\2\u00e2\u00e3\5$\23\2\u00e3\u00e9\3\2\2")
        buf.write("\2\u00e4\u00e5\f\4\2\2\u00e5\u00e6\7#\2\2\u00e6\u00e8")
        buf.write("\5$\23\2\u00e7\u00e4\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea#\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00ec\u00ed\b\23\1\2\u00ed\u00ee\5&\24")
        buf.write("\2\u00ee\u00f4\3\2\2\2\u00ef\u00f0\f\4\2\2\u00f0\u00f1")
        buf.write("\7\"\2\2\u00f1\u00f3\5&\24\2\u00f2\u00ef\3\2\2\2\u00f3")
        buf.write("\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5%\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\b\24\1")
        buf.write("\2\u00f8\u00f9\5(\25\2\u00f9\u00ff\3\2\2\2\u00fa\u00fb")
        buf.write("\f\4\2\2\u00fb\u00fc\t\5\2\2\u00fc\u00fe\5(\25\2\u00fd")
        buf.write("\u00fa\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\'\3\2\2\2\u0101\u00ff\3\2\2")
        buf.write("\2\u0102\u0103\b\25\1\2\u0103\u0104\5*\26\2\u0104\u010a")
        buf.write("\3\2\2\2\u0105\u0106\f\4\2\2\u0106\u0107\t\6\2\2\u0107")
        buf.write("\u0109\5*\26\2\u0108\u0105\3\2\2\2\u0109\u010c\3\2\2\2")
        buf.write("\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b)\3\2\2")
        buf.write("\2\u010c\u010a\3\2\2\2\u010d\u010e\b\26\1\2\u010e\u010f")
        buf.write("\5,\27\2\u010f\u0115\3\2\2\2\u0110\u0111\f\4\2\2\u0111")
        buf.write("\u0112\t\7\2\2\u0112\u0114\5,\27\2\u0113\u0110\3\2\2\2")
        buf.write("\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3")
        buf.write("\2\2\2\u0116+\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119")
        buf.write("\7$\2\2\u0119\u011e\5,\27\2\u011a\u011b\7\30\2\2\u011b")
        buf.write("\u011e\5,\27\2\u011c\u011e\5.\30\2\u011d\u0118\3\2\2\2")
        buf.write("\u011d\u011a\3\2\2\2\u011d\u011c\3\2\2\2\u011e-\3\2\2")
        buf.write("\2\u011f\u0120\b\30\1\2\u0120\u0121\5\60\31\2\u0121\u0134")
        buf.write("\3\2\2\2\u0122\u0123\f\6\2\2\u0123\u0124\7\62\2\2\u0124")
        buf.write("\u0125\5\"\22\2\u0125\u0126\7\63\2\2\u0126\u0133\3\2\2")
        buf.write("\2\u0127\u0128\f\5\2\2\u0128\u0129\7,\2\2\u0129\u0133")
        buf.write("\7\67\2\2\u012a\u012b\f\4\2\2\u012b\u012c\7,\2\2\u012c")
        buf.write("\u012d\7\67\2\2\u012d\u012f\7.\2\2\u012e\u0130\5\34\17")
        buf.write("\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131\u0133\7/\2\2\u0132\u0122\3\2\2\2\u0132")
        buf.write("\u0127\3\2\2\2\u0132\u012a\3\2\2\2\u0133\u0136\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135/\3\2\2")
        buf.write("\2\u0136\u0134\3\2\2\2\u0137\u0138\7\67\2\2\u0138\u0139")
        buf.write("\7.\2\2\u0139\u013a\5\"\22\2\u013a\u013b\7/\2\2\u013b")
        buf.write("\u0144\3\2\2\2\u013c\u013d\7.\2\2\u013d\u013e\5\"\22\2")
        buf.write("\u013e\u013f\7/\2\2\u013f\u0144\3\2\2\2\u0140\u0144\7")
        buf.write("\67\2\2\u0141\u0144\5\6\4\2\u0142\u0144\5\32\16\2\u0143")
        buf.write("\u0137\3\2\2\2\u0143\u013c\3\2\2\2\u0143\u0140\3\2\2\2")
        buf.write("\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144\61\3\2")
        buf.write("\2\2\u0145\u0146\7\67\2\2\u0146\u0147\5\64\33\2\u0147")
        buf.write("\63\3\2\2\2\u0148\u0149\7\62\2\2\u0149\u014a\5\"\22\2")
        buf.write("\u014a\u014b\7\63\2\2\u014b\u014c\5\64\33\2\u014c\u0152")
        buf.write("\3\2\2\2\u014d\u014e\7\62\2\2\u014e\u014f\5\"\22\2\u014f")
        buf.write("\u0150\7\63\2\2\u0150\u0152\3\2\2\2\u0151\u0148\3\2\2")
        buf.write("\2\u0151\u014d\3\2\2\2\u0152\65\3\2\2\2\u0153\u0154\b")
        buf.write("\34\1\2\u0154\u0155\58\35\2\u0155\u0156\7,\2\2\u0156\u0157")
        buf.write("\58\35\2\u0157\u015d\3\2\2\2\u0158\u0159\f\4\2\2\u0159")
        buf.write("\u015a\7,\2\2\u015a\u015c\58\35\2\u015b\u0158\3\2\2\2")
        buf.write("\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3")
        buf.write("\2\2\2\u015e\67\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0163")
        buf.write("\5\62\32\2\u0161\u0163\7\67\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u01639\3\2\2\2\u0164\u016a\5@!\2\u0165")
        buf.write("\u016a\5> \2\u0166\u016a\5F$\2\u0167\u016a\5J&\2\u0168")
        buf.write("\u016a\5L\'\2\u0169\u0164\3\2\2\2\u0169\u0165\3\2\2\2")
        buf.write("\u0169\u0166\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u0168\3")
        buf.write("\2\2\2\u016a;\3\2\2\2\u016b\u016c\5:\36\2\u016c\u016d")
        buf.write("\5<\37\2\u016d\u0170\3\2\2\2\u016e\u0170\5:\36\2\u016f")
        buf.write("\u016b\3\2\2\2\u016f\u016e\3\2\2\2\u0170=\3\2\2\2\u0171")
        buf.write("\u0172\7\20\2\2\u0172\u0174\7\67\2\2\u0173\u0175\5\b\5")
        buf.write("\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0177\7&\2\2\u0177\u0178\5\"\22\2\u0178")
        buf.write("\u0179\3\2\2\2\u0179\u017a\7\65\2\2\u017a\u0187\3\2\2")
        buf.write("\2\u017b\u017c\7\20\2\2\u017c\u017d\7\67\2\2\u017d\u017e")
        buf.write("\5\b\5\2\u017e\u017f\7\65\2\2\u017f\u0187\3\2\2\2\u0180")
        buf.write("\u0181\7\17\2\2\u0181\u0182\7\67\2\2\u0182\u0183\7&\2")
        buf.write("\2\u0183\u0184\5\"\22\2\u0184\u0185\7\65\2\2\u0185\u0187")
        buf.write("\3\2\2\2\u0186\u0171\3\2\2\2\u0186\u017b\3\2\2\2\u0186")
        buf.write("\u0180\3\2\2\2\u0187?\3\2\2\2\u0188\u0189\7\7\2\2\u0189")
        buf.write("\u018a\7\67\2\2\u018a\u018d\7.\2\2\u018b\u018e\5B\"\2")
        buf.write("\u018c\u018e\5P)\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2")
        buf.write("\2\2\u018e\u018f\3\2\2\2\u018f\u0191\7/\2\2\u0190\u0192")
        buf.write("\5\b\5\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193\u0194\7\60\2\2\u0194\u0196\5T+\2")
        buf.write("\u0195\u0197\5p9\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2")
        buf.write("\2\2\u0197\u0198\3\2\2\2\u0198\u0199\7\61\2\2\u0199\u019a")
        buf.write("\7\65\2\2\u019aA\3\2\2\2\u019b\u019e\5D#\2\u019c\u019e")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("C\3\2\2\2\u019f\u01a0\7\67\2\2\u01a0\u01a1\5\b\5\2\u01a1")
        buf.write("\u01a2\7\64\2\2\u01a2\u01a3\5D#\2\u01a3\u01a7\3\2\2\2")
        buf.write("\u01a4\u01a5\7\67\2\2\u01a5\u01a7\5\b\5\2\u01a6\u019f")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7E\3\2\2\2\u01a8\u01a9")
        buf.write("\7\b\2\2\u01a9\u01aa\7\67\2\2\u01aa\u01ab\7\t\2\2\u01ab")
        buf.write("\u01ac\7\60\2\2\u01ac\u01ad\5H%\2\u01ad\u01ae\7\61\2\2")
        buf.write("\u01ae\u01af\7\65\2\2\u01afG\3\2\2\2\u01b0\u01b1\7\67")
        buf.write("\2\2\u01b1\u01b2\5\b\5\2\u01b2\u01b3\7\65\2\2\u01b3\u01b4")
        buf.write("\5H%\2\u01b4\u01ba\3\2\2\2\u01b5\u01b6\7\67\2\2\u01b6")
        buf.write("\u01b7\5\b\5\2\u01b7\u01b8\7\65\2\2\u01b8\u01ba\3\2\2")
        buf.write("\2\u01b9\u01b0\3\2\2\2\u01b9\u01b5\3\2\2\2\u01baI\3\2")
        buf.write("\2\2\u01bb\u01bc\7\7\2\2\u01bc\u01bd\7.\2\2\u01bd\u01be")
        buf.write("\7\67\2\2\u01be\u01bf\7\67\2\2\u01bf\u01c0\7/\2\2\u01c0")
        buf.write("\u01c1\7\67\2\2\u01c1\u01c4\7.\2\2\u01c2\u01c5\5B\"\2")
        buf.write("\u01c3\u01c5\5P)\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2")
        buf.write("\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\7/\2\2\u01c7\u01c9")
        buf.write("\5\b\5\2\u01c8\u01c7\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01ca\u01cb\7\60\2\2\u01cb\u01cd\5T+\2")
        buf.write("\u01cc\u01ce\5p9\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce\3\2")
        buf.write("\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\7\61\2\2\u01d0\u01d1")
        buf.write("\7\65\2\2\u01d1K\3\2\2\2\u01d2\u01d3\7\b\2\2\u01d3\u01d4")
        buf.write("\7\67\2\2\u01d4\u01d5\7\n\2\2\u01d5\u01d6\7\60\2\2\u01d6")
        buf.write("\u01d7\5N(\2\u01d7\u01d8\7\61\2\2\u01d8\u01d9\7\65\2\2")
        buf.write("\u01d9M\3\2\2\2\u01da\u01db\7\67\2\2\u01db\u01dc\7.\2")
        buf.write("\2\u01dc\u01dd\5P)\2\u01dd\u01df\7/\2\2\u01de\u01e0\5")
        buf.write("\b\5\2\u01df\u01de\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1\u01e2\7\65\2\2\u01e2\u01e3\5N(\2\u01e3")
        buf.write("\u01ee\3\2\2\2\u01e4\u01e5\7\67\2\2\u01e5\u01e6\7.\2\2")
        buf.write("\u01e6\u01e7\5P)\2\u01e7\u01e9\7/\2\2\u01e8\u01ea\5\b")
        buf.write("\5\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write("\3\2\2\2\u01eb\u01ec\7\65\2\2\u01ec\u01ee\3\2\2\2\u01ed")
        buf.write("\u01da\3\2\2\2\u01ed\u01e4\3\2\2\2\u01eeO\3\2\2\2\u01ef")
        buf.write("\u01f2\5R*\2\u01f0\u01f2\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1")
        buf.write("\u01f0\3\2\2\2\u01f2Q\3\2\2\2\u01f3\u01f4\5\n\6\2\u01f4")
        buf.write("\u01f5\5\b\5\2\u01f5\u01f6\7\64\2\2\u01f6\u01f7\5R*\2")
        buf.write("\u01f7\u01fc\3\2\2\2\u01f8\u01f9\5\n\6\2\u01f9\u01fa\5")
        buf.write("\b\5\2\u01fa\u01fc\3\2\2\2\u01fb\u01f3\3\2\2\2\u01fb\u01f8")
        buf.write("\3\2\2\2\u01fcS\3\2\2\2\u01fd\u01fe\5V,\2\u01fe\u01ff")
        buf.write("\5T+\2\u01ff\u0202\3\2\2\2\u0200\u0202\5V,\2\u0201\u01fd")
        buf.write("\3\2\2\2\u0201\u0200\3\2\2\2\u0202U\3\2\2\2\u0203\u0209")
        buf.write("\5X-\2\u0204\u0209\5j\66\2\u0205\u0209\5n8\2\u0206\u0209")
        buf.write("\5l\67\2\u0207\u0209\5p9\2\u0208\u0203\3\2\2\2\u0208\u0204")
        buf.write("\3\2\2\2\u0208\u0205\3\2\2\2\u0208\u0206\3\2\2\2\u0208")
        buf.write("\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b\7\65\2")
        buf.write("\2\u020b\u0214\3\2\2\2\u020c\u020f\5\\/\2\u020d\u020f")
        buf.write("\5b\62\2\u020e\u020c\3\2\2\2\u020e\u020d\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u0210\u0211\7\65\2\2\u0211\u0214\3\2\2")
        buf.write("\2\u0212\u0214\5> \2\u0213\u0208\3\2\2\2\u0213\u020e\3")
        buf.write("\2\2\2\u0213\u0212\3\2\2\2\u0214W\3\2\2\2\u0215\u0216")
        buf.write("\5Z.\2\u0216\u0217\t\b\2\2\u0217\u0218\5\"\22\2\u0218")
        buf.write("Y\3\2\2\2\u0219\u021d\5\66\34\2\u021a\u021d\5\62\32\2")
        buf.write("\u021b\u021d\7\67\2\2\u021c\u0219\3\2\2\2\u021c\u021a")
        buf.write("\3\2\2\2\u021c\u021b\3\2\2\2\u021d[\3\2\2\2\u021e\u021f")
        buf.write("\7\3\2\2\u021f\u0220\7.\2\2\u0220\u0221\5\"\22\2\u0221")
        buf.write("\u0222\7/\2\2\u0222\u0223\3\2\2\2\u0223\u0224\7\60\2\2")
        buf.write("\u0224\u0225\5T+\2\u0225\u0227\7\61\2\2\u0226\u0228\5")
        buf.write("^\60\2\u0227\u0226\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u022a")
        buf.write("\3\2\2\2\u0229\u022b\5`\61\2\u022a\u0229\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022b]\3\2\2\2\u022c\u022d\7\4\2\2\u022d")
        buf.write("\u022e\7\3\2\2\u022e\u022f\7.\2\2\u022f\u0230\5\"\22\2")
        buf.write("\u0230\u0231\7/\2\2\u0231\u0232\3\2\2\2\u0232\u0233\7")
        buf.write("\60\2\2\u0233\u0234\5T+\2\u0234\u0236\7\61\2\2\u0235\u0237")
        buf.write("\5^\60\2\u0236\u0235\3\2\2\2\u0236\u0237\3\2\2\2\u0237")
        buf.write("\u0243\3\2\2\2\u0238\u0239\7\4\2\2\u0239\u023a\7\3\2\2")
        buf.write("\u023a\u023b\7.\2\2\u023b\u023c\5\"\22\2\u023c\u023d\7")
        buf.write("/\2\2\u023d\u023e\3\2\2\2\u023e\u023f\7\60\2\2\u023f\u0240")
        buf.write("\5T+\2\u0240\u0241\7\61\2\2\u0241\u0243\3\2\2\2\u0242")
        buf.write("\u022c\3\2\2\2\u0242\u0238\3\2\2\2\u0243_\3\2\2\2\u0244")
        buf.write("\u0245\7\4\2\2\u0245\u0246\7\60\2\2\u0246\u0247\5T+\2")
        buf.write("\u0247\u0248\7\61\2\2\u0248a\3\2\2\2\u0249\u024a\7\5\2")
        buf.write("\2\u024a\u024b\5d\63\2\u024b\u024c\7\60\2\2\u024c\u024d")
        buf.write("\5T+\2\u024d\u024e\7\61\2\2\u024ec\3\2\2\2\u024f\u0252")
        buf.write("\5f\64\2\u0250\u0252\5h\65\2\u0251\u024f\3\2\2\2\u0251")
        buf.write("\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0255\7\65\2")
        buf.write("\2\u0254\u0256\5\"\22\2\u0255\u0254\3\2\2\2\u0255\u0256")
        buf.write("\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0259\7\65\2\2\u0258")
        buf.write("\u025a\5f\64\2\u0259\u0258\3\2\2\2\u0259\u025a\3\2\2\2")
        buf.write("\u025a\u0263\3\2\2\2\u025b\u025c\t\t\2\2\u025c\u025d\7")
        buf.write("\64\2\2\u025d\u025e\7\67\2\2\u025e\u025f\7%\2\2\u025f")
        buf.write("\u0260\7\23\2\2\u0260\u0263\5\"\22\2\u0261\u0263\5\"\22")
        buf.write("\2\u0262\u0251\3\2\2\2\u0262\u025b\3\2\2\2\u0262\u0261")
        buf.write("\3\2\2\2\u0263e\3\2\2\2\u0264\u0265\7\67\2\2\u0265\u0266")
        buf.write("\t\b\2\2\u0266\u0267\5\"\22\2\u0267g\3\2\2\2\u0268\u0269")
        buf.write("\7\20\2\2\u0269\u026b\7\67\2\2\u026a\u026c\5\b\5\2\u026b")
        buf.write("\u026a\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026d\3\2\2\2")
        buf.write("\u026d\u026e\7&\2\2\u026e\u026f\5\"\22\2\u026fi\3\2\2")
        buf.write("\2\u0270\u0271\7\22\2\2\u0271k\3\2\2\2\u0272\u0273\7\21")
        buf.write("\2\2\u0273m\3\2\2\2\u0274\u0277\5\32\16\2\u0275\u0277")
        buf.write("\5\36\20\2\u0276\u0274\3\2\2\2\u0276\u0275\3\2\2\2\u0277")
        buf.write("o\3\2\2\2\u0278\u027a\7\6\2\2\u0279\u027b\5\"\22\2\u027a")
        buf.write("\u0279\3\2\2\2\u027a\u027b\3\2\2\2\u027bq\3\2\2\2>\177")
        buf.write("\u0089\u008f\u009e\u00a5\u00ad\u00b6\u00c1\u00c6\u00cf")
        buf.write("\u00d6\u00dc\u00df\u00e9\u00f4\u00ff\u010a\u0115\u011d")
        buf.write("\u012f\u0132\u0134\u0143\u0151\u015d\u0162\u0169\u016f")
        buf.write("\u0174\u0186\u018d\u0191\u0196\u019d\u01a6\u01b9\u01c4")
        buf.write("\u01c8\u01cd\u01df\u01e9\u01ed\u01f1\u01fb\u0201\u0208")
        buf.write("\u020e\u0213\u021c\u0227\u022a\u0236\u0242\u0251\u0255")
        buf.write("\u0259\u0262\u026b\u0276\u027a")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "':='", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'_'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "COM_EQ", "COM_UEQ", "COM_LT", "COM_LEQ", "COM_GT", 
                      "COM_GEQ", "AND", "OR", "NOT", "ASSIGN", "EQ", "PLUS_EQ", 
                      "MINUS_EQ", "MUL_EQ", "DIV_EQ", "MOD_EQ", "DOT", "UNDER", 
                      "LCB", "RCB", "LSB", "RSB", "LB", "RB", "COMMA", "SEMI", 
                      "COLON", "ID", "INTEGER_LIT", "FLOAT_LIT", "BOOL_LIT", 
                      "STRING_LIT", "COMMENT_INLINE", "COMMENT_INBLOCK", 
                      "WS", "NL", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_primitive_literals = 1
    RULE_literal = 2
    RULE_types = 3
    RULE_idlist = 4
    RULE_array_literals = 5
    RULE_array_type = 6
    RULE_element_list = 7
    RULE_element = 8
    RULE_struct_literals = 9
    RULE_struct_attlist = 10
    RULE_struct_attlist_prime = 11
    RULE_func_call = 12
    RULE_list_expression = 13
    RULE_method_call = 14
    RULE_dot_operator = 15
    RULE_expression = 16
    RULE_expression1 = 17
    RULE_expression2 = 18
    RULE_expression3 = 19
    RULE_expression4 = 20
    RULE_expression5 = 21
    RULE_expression6 = 22
    RULE_expression7 = 23
    RULE_array_access = 24
    RULE_array_op = 25
    RULE_struct_access = 26
    RULE_fieldname = 27
    RULE_decl = 28
    RULE_decls = 29
    RULE_vardecl = 30
    RULE_funcdecl = 31
    RULE_paramlist = 32
    RULE_paramlist_prime = 33
    RULE_struct_decl = 34
    RULE_declist = 35
    RULE_method_decl = 36
    RULE_interface_decl = 37
    RULE_decl_list1 = 38
    RULE_paramlist1 = 39
    RULE_paramlist1_prime = 40
    RULE_stmts = 41
    RULE_stmt = 42
    RULE_assign_stmt = 43
    RULE_variable = 44
    RULE_if_stmt = 45
    RULE_elseif_stmt = 46
    RULE_else_stmt = 47
    RULE_for_stmt = 48
    RULE_condition = 49
    RULE_assign_stmtfor = 50
    RULE_vardeclfor = 51
    RULE_break_stmt = 52
    RULE_continue_stmt = 53
    RULE_call_stmt = 54
    RULE_return_stmt = 55

    ruleNames =  [ "program", "primitive_literals", "literal", "types", 
                   "idlist", "array_literals", "array_type", "element_list", 
                   "element", "struct_literals", "struct_attlist", "struct_attlist_prime", 
                   "func_call", "list_expression", "method_call", "dot_operator", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "array_access", "array_op", "struct_access", "fieldname", 
                   "decl", "decls", "vardecl", "funcdecl", "paramlist", 
                   "paramlist_prime", "struct_decl", "declist", "method_decl", 
                   "interface_decl", "decl_list1", "paramlist1", "paramlist1_prime", 
                   "stmts", "stmt", "assign_stmt", "variable", "if_stmt", 
                   "elseif_stmt", "else_stmt", "for_stmt", "condition", 
                   "assign_stmtfor", "vardeclfor", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    COM_EQ=26
    COM_UEQ=27
    COM_LT=28
    COM_LEQ=29
    COM_GT=30
    COM_GEQ=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    EQ=36
    PLUS_EQ=37
    MINUS_EQ=38
    MUL_EQ=39
    DIV_EQ=40
    MOD_EQ=41
    DOT=42
    UNDER=43
    LCB=44
    RCB=45
    LSB=46
    RSB=47
    LB=48
    RB=49
    COMMA=50
    SEMI=51
    COLON=52
    ID=53
    INTEGER_LIT=54
    FLOAT_LIT=55
    BOOL_LIT=56
    STRING_LIT=57
    COMMENT_INLINE=58
    COMMENT_INBLOCK=59
    WS=60
    NL=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(MiniGoParser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.decls()
            self.state = 113
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_literalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(MiniGoParser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_literals" ):
                return visitor.visitPrimitive_literals(self)
            else:
                return visitor.visitChildren(self)




    def primitive_literals(self):

        localctx = MiniGoParser.Primitive_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primitive_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTEGER_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(MiniGoParser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def array_literals(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalsContext,0)


        def struct_literals(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(MiniGoParser.INTEGER_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 122
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 123
                self.array_literals()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 124
                self.struct_literals()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_types)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.array_type()
                self.state = 128
                self.types()
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MiniGoParser.IdlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MiniGoParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idlist)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(MiniGoParser.ID)
                self.state = 138
                self.match(MiniGoParser.COMMA)
                self.state = 139
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literals" ):
                return visitor.visitArray_literals(self)
            else:
                return visitor.visitChildren(self)




    def array_literals(self):

        localctx = MiniGoParser.Array_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.array_type()
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 145
            self.match(MiniGoParser.LSB)
            self.state = 146
            self.element_list()
            self.state = 147
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def INTEGER_LIT(self):
            return self.getToken(MiniGoParser.INTEGER_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(MiniGoParser.LB)
                self.state = 150
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTEGER_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self.match(MiniGoParser.RB)
                self.state = 152
                self.array_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(MiniGoParser.LB)
                self.state = 154
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTEGER_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.match(MiniGoParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_list" ):
                return visitor.visitElement_list(self)
            else:
                return visitor.visitChildren(self)




    def element_list(self):

        localctx = MiniGoParser.Element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_element_list)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.element()
                self.state = 159
                self.match(MiniGoParser.COMMA)
                self.state = 160
                self.element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_literals(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_literalsContext,0)


        def struct_literals(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalsContext,0)


        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_element)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.primitive_literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.struct_literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(MiniGoParser.LSB)
                self.state = 168
                self.element_list()
                self.state = 169
                self.match(MiniGoParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def struct_attlist(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_attlistContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literals" ):
                return visitor.visitStruct_literals(self)
            else:
                return visitor.visitChildren(self)




    def struct_literals(self):

        localctx = MiniGoParser.Struct_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_struct_literals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MiniGoParser.ID)
            self.state = 174
            self.match(MiniGoParser.LSB)
            self.state = 175
            self.struct_attlist()
            self.state = 176
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_attlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_attlist_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_attlist_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_attlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_attlist" ):
                return visitor.visitStruct_attlist(self)
            else:
                return visitor.visitChildren(self)




    def struct_attlist(self):

        localctx = MiniGoParser.Struct_attlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_struct_attlist)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.struct_attlist_prime()
                pass
            elif token in [MiniGoParser.RSB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_attlist_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def struct_attlist_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_attlist_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_attlist_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_attlist_prime" ):
                return visitor.visitStruct_attlist_prime(self)
            else:
                return visitor.visitChildren(self)




    def struct_attlist_prime(self):

        localctx = MiniGoParser.Struct_attlist_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_struct_attlist_prime)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(MiniGoParser.ID)
                self.state = 183
                self.match(MiniGoParser.COLON)
                self.state = 184
                self.expression(0)
                self.state = 185
                self.match(MiniGoParser.COMMA)
                self.state = 186
                self.struct_attlist_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(MiniGoParser.ID)
                self.state = 189
                self.match(MiniGoParser.COLON)
                self.state = 190
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.ID)
            self.state = 194
            self.match(MiniGoParser.LCB)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTEGER_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 195
                self.list_expression()


            self.state = 198
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_expression)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.expression(0)
                self.state = 201
                self.match(MiniGoParser.COMMA)
                self.state = 202
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dot_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Dot_operatorContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.dot_operator()
            self.state = 208
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dot_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def dot_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Dot_operatorContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dot_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot_operator" ):
                return visitor.visitDot_operator(self)
            else:
                return visitor.visitChildren(self)




    def dot_operator(self):

        localctx = MiniGoParser.Dot_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dot_operator)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 210
                    self.match(MiniGoParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 211
                    self.array_access()
                    pass


                self.state = 214
                self.match(MiniGoParser.DOT)
                self.state = 215
                self.dot_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 216
                    self.match(MiniGoParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 217
                    self.array_access()
                    pass


                self.state = 220
                self.match(MiniGoParser.DOT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 226
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 227
                    self.match(MiniGoParser.OR)
                    self.state = 228
                    self.expression1(0) 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 238
                    self.match(MiniGoParser.AND)
                    self.state = 239
                    self.expression2(0) 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def COM_EQ(self):
            return self.getToken(MiniGoParser.COM_EQ, 0)

        def COM_GEQ(self):
            return self.getToken(MiniGoParser.COM_GEQ, 0)

        def COM_GT(self):
            return self.getToken(MiniGoParser.COM_GT, 0)

        def COM_LEQ(self):
            return self.getToken(MiniGoParser.COM_LEQ, 0)

        def COM_LT(self):
            return self.getToken(MiniGoParser.COM_LT, 0)

        def COM_UEQ(self):
            return self.getToken(MiniGoParser.COM_UEQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 248
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 249
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.COM_EQ) | (1 << MiniGoParser.COM_UEQ) | (1 << MiniGoParser.COM_LT) | (1 << MiniGoParser.COM_LEQ) | (1 << MiniGoParser.COM_GT) | (1 << MiniGoParser.COM_GEQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 250
                    self.expression3(0) 
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 259
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 260
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 261
                    self.expression4(0) 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 270
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 271
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 272
                    self.expression5() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression5)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(MiniGoParser.NOT)
                self.state = 279
                self.expression5()
                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(MiniGoParser.SUB)
                self.state = 281
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LCB, MiniGoParser.LB, MiniGoParser.ID, MiniGoParser.INTEGER_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 304
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 288
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 289
                        self.match(MiniGoParser.LB)
                        self.state = 290
                        self.expression(0)
                        self.state = 291
                        self.match(MiniGoParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 293
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 294
                        self.match(MiniGoParser.DOT)
                        self.state = 295
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 296
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 297
                        self.match(MiniGoParser.DOT)
                        self.state = 298
                        self.match(MiniGoParser.ID)
                        self.state = 299
                        self.match(MiniGoParser.LCB)
                        self.state = 301
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTEGER_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 300
                            self.list_expression()


                        self.state = 303
                        self.match(MiniGoParser.RCB)
                        pass

             
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression7)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(MiniGoParser.ID)
                self.state = 310
                self.match(MiniGoParser.LCB)
                self.state = 311
                self.expression(0)
                self.state = 312
                self.match(MiniGoParser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.match(MiniGoParser.LCB)
                self.state = 315
                self.expression(0)
                self.state = 316
                self.match(MiniGoParser.RCB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 319
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 320
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_op(self):
            return self.getTypedRuleContext(MiniGoParser.Array_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(MiniGoParser.ID)
            self.state = 324
            self.array_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def array_op(self):
            return self.getTypedRuleContext(MiniGoParser.Array_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_op" ):
                return visitor.visitArray_op(self)
            else:
                return visitor.visitChildren(self)




    def array_op(self):

        localctx = MiniGoParser.Array_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_op)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(MiniGoParser.LB)
                self.state = 327
                self.expression(0)
                self.state = 328
                self.match(MiniGoParser.RB)
                self.state = 329
                self.array_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(MiniGoParser.LB)
                self.state = 332
                self.expression(0)
                self.state = 333
                self.match(MiniGoParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FieldnameContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FieldnameContext,i)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)



    def struct_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_struct_access, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.fieldname()
            self.state = 339
            self.match(MiniGoParser.DOT)
            self.state = 340
            self.fieldname()
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_access)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    self.match(MiniGoParser.DOT)
                    self.state = 344
                    self.fieldname() 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FieldnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldname" ):
                return visitor.visitFieldname(self)
            else:
                return visitor.visitChildren(self)




    def fieldname(self):

        localctx = MiniGoParser.FieldnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_fieldname)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.array_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_decl)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.struct_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.method_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                self.interface_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(MiniGoParser.DeclsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MiniGoParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_decls)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.decl()
                self.state = 362
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(MiniGoParser.VAR)
                self.state = 368
                self.match(MiniGoParser.ID)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 369
                    self.types()


                self.state = 372
                self.match(MiniGoParser.EQ)
                self.state = 373
                self.expression(0)

                self.state = 375
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.match(MiniGoParser.VAR)
                self.state = 378
                self.match(MiniGoParser.ID)
                self.state = 379
                self.types()

                self.state = 380
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 382
                self.match(MiniGoParser.CONST)
                self.state = 383
                self.match(MiniGoParser.ID)
                self.state = 384
                self.match(MiniGoParser.EQ)
                self.state = 385
                self.expression(0)

                self.state = 386
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def stmts(self):
            return self.getTypedRuleContext(MiniGoParser.StmtsContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def paramlist1(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist1Context,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MiniGoParser.FUNC)
            self.state = 391
            self.match(MiniGoParser.ID)
            self.state = 392
            self.match(MiniGoParser.LCB)
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 393
                self.paramlist()
                pass

            elif la_ == 2:
                self.state = 394
                self.paramlist1()
                pass


            self.state = 397
            self.match(MiniGoParser.RCB)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 398
                self.types()


            self.state = 401
            self.match(MiniGoParser.LSB)
            self.state = 402
            self.stmts()
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.RETURN:
                self.state = 403
                self.return_stmt()


            self.state = 406
            self.match(MiniGoParser.RSB)

            self.state = 407
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlist_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MiniGoParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_paramlist)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.paramlist_prime()
                pass
            elif token in [MiniGoParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramlist_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramlist_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist_prime" ):
                return visitor.visitParamlist_prime(self)
            else:
                return visitor.visitChildren(self)




    def paramlist_prime(self):

        localctx = MiniGoParser.Paramlist_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_paramlist_prime)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(MiniGoParser.ID)
                self.state = 414
                self.types()
                self.state = 415
                self.match(MiniGoParser.COMMA)
                self.state = 416
                self.paramlist_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.match(MiniGoParser.ID)
                self.state = 419
                self.types()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def declist(self):
            return self.getTypedRuleContext(MiniGoParser.DeclistContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.TYPE)
            self.state = 423
            self.match(MiniGoParser.ID)
            self.state = 424
            self.match(MiniGoParser.STRUCT)
            self.state = 425
            self.match(MiniGoParser.LSB)
            self.state = 426
            self.declist()
            self.state = 427
            self.match(MiniGoParser.RSB)

            self.state = 428
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def declist(self):
            return self.getTypedRuleContext(MiniGoParser.DeclistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclist" ):
                return visitor.visitDeclist(self)
            else:
                return visitor.visitChildren(self)




    def declist(self):

        localctx = MiniGoParser.DeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_declist)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(MiniGoParser.ID)
                self.state = 431
                self.types()
                self.state = 432
                self.match(MiniGoParser.SEMI)
                self.state = 433
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(MiniGoParser.ID)
                self.state = 436
                self.types()
                self.state = 437
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LCB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LCB)
            else:
                return self.getToken(MiniGoParser.LCB, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RCB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RCB)
            else:
                return self.getToken(MiniGoParser.RCB, i)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def stmts(self):
            return self.getTypedRuleContext(MiniGoParser.StmtsContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def paramlist1(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist1Context,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(MiniGoParser.FUNC)
            self.state = 442
            self.match(MiniGoParser.LCB)
            self.state = 443
            self.match(MiniGoParser.ID)
            self.state = 444
            self.match(MiniGoParser.ID)
            self.state = 445
            self.match(MiniGoParser.RCB)
            self.state = 446
            self.match(MiniGoParser.ID)
            self.state = 447
            self.match(MiniGoParser.LCB)
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 448
                self.paramlist()
                pass

            elif la_ == 2:
                self.state = 449
                self.paramlist1()
                pass


            self.state = 452
            self.match(MiniGoParser.RCB)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 453
                self.types()


            self.state = 456
            self.match(MiniGoParser.LSB)
            self.state = 457
            self.stmts()
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.RETURN:
                self.state = 458
                self.return_stmt()


            self.state = 461
            self.match(MiniGoParser.RSB)

            self.state = 462
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def decl_list1(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_list1Context,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(MiniGoParser.TYPE)
            self.state = 465
            self.match(MiniGoParser.ID)
            self.state = 466
            self.match(MiniGoParser.INTERFACE)
            self.state = 467
            self.match(MiniGoParser.LSB)
            self.state = 468
            self.decl_list1()
            self.state = 469
            self.match(MiniGoParser.RSB)

            self.state = 470
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_list1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def paramlist1(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist1Context,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def decl_list1(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_list1Context,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_list1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list1" ):
                return visitor.visitDecl_list1(self)
            else:
                return visitor.visitChildren(self)




    def decl_list1(self):

        localctx = MiniGoParser.Decl_list1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_decl_list1)
        self._la = 0 # Token type
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(MiniGoParser.ID)
                self.state = 473
                self.match(MiniGoParser.LCB)
                self.state = 474
                self.paramlist1()
                self.state = 475
                self.match(MiniGoParser.RCB)
                self.state = 477
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 476
                    self.types()


                self.state = 479
                self.match(MiniGoParser.SEMI)
                self.state = 480
                self.decl_list1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.match(MiniGoParser.ID)
                self.state = 483
                self.match(MiniGoParser.LCB)
                self.state = 484
                self.paramlist1()
                self.state = 485
                self.match(MiniGoParser.RCB)
                self.state = 487
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 486
                    self.types()


                self.state = 489
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramlist1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlist1_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist1_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist1" ):
                return visitor.visitParamlist1(self)
            else:
                return visitor.visitChildren(self)




    def paramlist1(self):

        localctx = MiniGoParser.Paramlist1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_paramlist1)
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.paramlist1_prime()
                pass
            elif token in [MiniGoParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramlist1_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MiniGoParser.IdlistContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramlist1_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Paramlist1_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist1_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist1_prime" ):
                return visitor.visitParamlist1_prime(self)
            else:
                return visitor.visitChildren(self)




    def paramlist1_prime(self):

        localctx = MiniGoParser.Paramlist1_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_paramlist1_prime)
        try:
            self.state = 505
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.idlist()
                self.state = 498
                self.types()
                self.state = 499
                self.match(MiniGoParser.COMMA)
                self.state = 500
                self.paramlist1_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.idlist()
                self.state = 503
                self.types()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmts(self):
            return self.getTypedRuleContext(MiniGoParser.StmtsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = MiniGoParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmts)
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.stmt()
                self.state = 508
                self.stmts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_stmt)
        try:
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 513
                    self.assign_stmt()
                    pass

                elif la_ == 2:
                    self.state = 514
                    self.break_stmt()
                    pass

                elif la_ == 3:
                    self.state = 515
                    self.call_stmt()
                    pass

                elif la_ == 4:
                    self.state = 516
                    self.continue_stmt()
                    pass

                elif la_ == 5:
                    self.state = 517
                    self.return_stmt()
                    pass


                self.state = 520
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.IF, MiniGoParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF]:
                    self.state = 522
                    self.if_stmt()
                    pass
                elif token in [MiniGoParser.FOR]:
                    self.state = 523
                    self.for_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 526
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 528
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(MiniGoParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def PLUS_EQ(self):
            return self.getToken(MiniGoParser.PLUS_EQ, 0)

        def MINUS_EQ(self):
            return self.getToken(MiniGoParser.MINUS_EQ, 0)

        def MUL_EQ(self):
            return self.getToken(MiniGoParser.MUL_EQ, 0)

        def MOD_EQ(self):
            return self.getToken(MiniGoParser.MOD_EQ, 0)

        def DIV_EQ(self):
            return self.getToken(MiniGoParser.DIV_EQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.variable()
            self.state = 532
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_EQ) | (1 << MiniGoParser.MINUS_EQ) | (1 << MiniGoParser.MUL_EQ) | (1 << MiniGoParser.DIV_EQ) | (1 << MiniGoParser.MOD_EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 533
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = MiniGoParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_variable)
        try:
            self.state = 538
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.struct_access(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 537
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def stmts(self):
            return self.getTypedRuleContext(MiniGoParser.StmtsContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def elseif_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_stmtContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(MiniGoParser.IF)

            self.state = 541
            self.match(MiniGoParser.LCB)
            self.state = 542
            self.expression(0)
            self.state = 543
            self.match(MiniGoParser.RCB)
            self.state = 545
            self.match(MiniGoParser.LSB)
            self.state = 546
            self.stmts()
            self.state = 547
            self.match(MiniGoParser.RSB)
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 548
                self.elseif_stmt()


            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 551
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def stmts(self):
            return self.getTypedRuleContext(MiniGoParser.StmtsContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def elseif_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = MiniGoParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_elseif_stmt)
        try:
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.match(MiniGoParser.ELSE)
                self.state = 555
                self.match(MiniGoParser.IF)

                self.state = 556
                self.match(MiniGoParser.LCB)
                self.state = 557
                self.expression(0)
                self.state = 558
                self.match(MiniGoParser.RCB)
                self.state = 560
                self.match(MiniGoParser.LSB)
                self.state = 561
                self.stmts()
                self.state = 562
                self.match(MiniGoParser.RSB)
                self.state = 564
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 563
                    self.elseif_stmt()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.match(MiniGoParser.ELSE)
                self.state = 567
                self.match(MiniGoParser.IF)

                self.state = 568
                self.match(MiniGoParser.LCB)
                self.state = 569
                self.expression(0)
                self.state = 570
                self.match(MiniGoParser.RCB)
                self.state = 572
                self.match(MiniGoParser.LSB)
                self.state = 573
                self.stmts()
                self.state = 574
                self.match(MiniGoParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def stmts(self):
            return self.getTypedRuleContext(MiniGoParser.StmtsContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.match(MiniGoParser.ELSE)
            self.state = 579
            self.match(MiniGoParser.LSB)
            self.state = 580
            self.stmts()
            self.state = 581
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def stmts(self):
            return self.getTypedRuleContext(MiniGoParser.StmtsContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(MiniGoParser.FOR)
            self.state = 584
            self.condition()
            self.state = 585
            self.match(MiniGoParser.LSB)
            self.state = 586
            self.stmts()
            self.state = 587
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def assign_stmtfor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assign_stmtforContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assign_stmtforContext,i)


        def vardeclfor(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclforContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def UNDER(self):
            return self.getToken(MiniGoParser.UNDER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 608
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ID]:
                    self.state = 589
                    self.assign_stmtfor()
                    pass
                elif token in [MiniGoParser.VAR]:
                    self.state = 590
                    self.vardeclfor()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 593
                self.match(MiniGoParser.SEMI)
                self.state = 595
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTEGER_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 594
                    self.expression(0)


                self.state = 597
                self.match(MiniGoParser.SEMI)
                self.state = 599
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 598
                    self.assign_stmtfor()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.UNDER or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 602
                self.match(MiniGoParser.COMMA)
                self.state = 603
                self.match(MiniGoParser.ID)
                self.state = 604
                self.match(MiniGoParser.ASSIGN)
                self.state = 605
                self.match(MiniGoParser.RANGE)
                self.state = 606
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 607
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def PLUS_EQ(self):
            return self.getToken(MiniGoParser.PLUS_EQ, 0)

        def MINUS_EQ(self):
            return self.getToken(MiniGoParser.MINUS_EQ, 0)

        def MUL_EQ(self):
            return self.getToken(MiniGoParser.MUL_EQ, 0)

        def MOD_EQ(self):
            return self.getToken(MiniGoParser.MOD_EQ, 0)

        def DIV_EQ(self):
            return self.getToken(MiniGoParser.DIV_EQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmtfor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmtfor" ):
                return visitor.visitAssign_stmtfor(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmtfor(self):

        localctx = MiniGoParser.Assign_stmtforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_assign_stmtfor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            self.match(MiniGoParser.ID)
            self.state = 611
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_EQ) | (1 << MiniGoParser.MINUS_EQ) | (1 << MiniGoParser.MUL_EQ) | (1 << MiniGoParser.DIV_EQ) | (1 << MiniGoParser.MOD_EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 612
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardeclfor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclfor" ):
                return visitor.visitVardeclfor(self)
            else:
                return visitor.visitChildren(self)




    def vardeclfor(self):

        localctx = MiniGoParser.VardeclforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_vardeclfor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.match(MiniGoParser.VAR)
            self.state = 615
            self.match(MiniGoParser.ID)
            self.state = 617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 616
                self.types()


            self.state = 619
            self.match(MiniGoParser.EQ)
            self.state = 620
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_call_stmt)
        try:
            self.state = 628
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 627
                self.method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self.match(MiniGoParser.RETURN)
            self.state = 632
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INTEGER_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 631
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression_sempred
        self._predicates[17] = self.expression1_sempred
        self._predicates[18] = self.expression2_sempred
        self._predicates[19] = self.expression3_sempred
        self._predicates[20] = self.expression4_sempred
        self._predicates[22] = self.expression6_sempred
        self._predicates[26] = self.struct_access_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def struct_access_sempred(self, localctx:Struct_accessContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




