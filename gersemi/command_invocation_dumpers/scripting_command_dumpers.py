from .argument_aware_command_invocation_dumper import (
    ArgumentAwareCommandInvocationDumper,
)
from .multiple_signature_command_invocation_dumper import (
    MultipleSignatureCommandInvocationDumper,
)


class CMakeHostSysteInformationCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["RESULT"]
    multi_value_keywords = ["QUERY"]


class CMakeParseArgumentsCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["PARSE_ARGV"]


class ConfigureFileCommandDumper(ArgumentAwareCommandInvocationDumper):
    front_positional_args = 2
    options = ["COPYONLY", "ESCAPE_QUOTES", "@ONLY"]
    one_value_keywords = ["NEWLINE_STYLE"]


class EndForeachCommandDumper(ArgumentAwareCommandInvocationDumper):
    pass


class EndFunctionCommandDumper(ArgumentAwareCommandInvocationDumper):
    pass


class EndMacroCommandDumper(ArgumentAwareCommandInvocationDumper):
    pass


class ExecuteProcessCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = [
        "OUTPUT_QUIET",
        "ERROR_QUIET",
        "OUTPUT_STRIP_TRAILING_WHITESPACE",
        "ERROR_STRIP_TRAILING_WHITESPACE",
    ]
    one_value_keywords = [
        "WORKING_DIRECTORY",
        "TIMEOUT",
        "RESULT_VARIABLE",
        "RESULTS_VARIABLE",
        "OUTPUT_VARIABLE",
        "ERROR_VARIABLE",
        "INPUT_FILE",
        "OUTPUT_FILE",
        "ERROR_FILE",
        "COMMAND_ECHO",
        "ENCODING",
    ]
    multi_value_keywords = ["COMMAND"]


class FileCommandDumper(MultipleSignatureCommandInvocationDumper):
    customized_signatures = {
        # Reading
        "READ": dict(
            options=["HEX"],
            one_value_keywords=["OFFSET", "LIMIT"],
            multi_value_keywords=["READ"],
        ),
        "STRINGS": dict(
            options=["NEWLINE_CONSUME", "NO_HEX_CONVERSION"],
            one_value_keywords=[
                "LENGTH_MAXIMUM",
                "LENGTH_MINIMUM",
                "LIMIT_COUNT",
                "LIMIT_INPUT",
                "LIMIT_OUTPUT",
                "REGEX",
                "ENCODING",
            ],
            multi_value_keywords=["STRINGS"],
        ),
        "GET_RUNTIME_DEPENDENCIES": dict(
            front_positional_args=1,
            one_value_keywords=[
                "RESOLVED_DEPENDENCIES_VAR",
                "UNRESOLVED_DEPENDENCIES_VAR",
                "CONFLICTING_DEPENDENCIES_PREFIX",
                "BUNDLE_EXECUTABLE",
            ],
            multi_value_keywords=[
                "EXECUTABLES",
                "LIBRARIES",
                "MODULES",
                "DIRECTORIES",
                "PRE_INCLUDE_REGEXES",
                "PRE_EXCLUDE_REGEXES",
                "POST_INCLUDE_REGEXES",
                "POST_EXCLUDE_REGEXES",
            ],
        ),
        # Writing
        "GENERATE": dict(
            one_value_keywords=["INPUT", "CONTENT", "CONDITION"],
            multi_value_keywords=["GENERATE"],
        ),
        # Filesystem
        "GLOB": dict(
            options=["CONFIGURE_DEPENDS"],
            one_value_keywords=["GLOB", "LIST_DIRECTORIES", "RELATIVE"],
        ),
        "GLOB_RECURSE": dict(
            options=["CONFIGURE_DEPENDS"],
            one_value_keywords=["GLOB_RECURSE", "LIST_DIRECTORIES", "RELATIVE"],
        ),
        "COPY": dict(
            options=[
                "NO_SOURCE_PERMISSIONS",
                "USE_SOURCE_PERMISSIONS",
                "FOLLOW_SYMLINK_CHAIN",
                "FILES_MATCHING",
                "EXCLUDE",
            ],
            one_value_keywords=["DESTINATION", "PATTERN", "REGEX"],
            multi_value_keywords=[
                "COPY",
                "FILE_PERMISSIONS",
                "DIRECTORY_PERMISSIONS",
                "PERMISSIONS",
            ],
        ),
        "INSTALL": dict(
            options=[
                "NO_SOURCE_PERMISSIONS",
                "USE_SOURCE_PERMISSIONS",
                "FOLLOW_SYMLINK_CHAIN",
                "FILES_MATCHING",
                "EXCLUDE",
            ],
            one_value_keywords=["DESTINATION", "PATTERN", "REGEX"],
            multi_value_keywords=[
                "INSTALL",
                "FILE_PERMISSIONS",
                "DIRECTORY_PERMISSIONS",
                "PERMISSIONS",
            ],
        ),
        "CREATE_LINK": dict(
            options=["COPY_ON_ERROR", "SYMBOLIC"],
            one_value_keywords=["RESULT"],
            multi_value_keywords=["CREATE_LINK"],
        ),
        # Transfer
        "DOWNLOAD": dict(
            options=["SHOW_PROGRESS"],
            one_value_keywords=[
                "INACTIVITY_TIMEOUT",
                "LOG",
                "STATUS",
                "TIMEOUT",
                "USERPWD",
                "HTTPHEADER",
                "NETRC",
                "NETRC_FILE",
                "EXPECTED_HASH",
                "EXPECTED_MD5",
                "TLS_VERIFY",
                "TLS_CAINFO",
            ],
            multi_value_keywords=["DOWNLOAD"],
        ),
        "UPLOAD": dict(
            options=["SHOW_PROGRESS"],
            one_value_keywords=[
                "INACTIVITY_TIMEOUT",
                "LOG",
                "STATUS",
                "TIMEOUT",
                "USERPWD",
                "HTTPHEADER",
                "NETRC",
                "NETRC_FILE",
            ],
            multi_value_keywords=["UPLOAD"],
        ),
        # Locking
        "LOCK": dict(
            options=["DIRECTORY", "RELEASE"],
            one_value_keywords=["LOCK", "GUARD", "RESULT_VARIABLE", "TIMEOUT"],
        ),
    }


class ForeachCommandDumper(ArgumentAwareCommandInvocationDumper):
    front_positional_args = 1
    options = ["IN"]
    multi_value_keywords = ["RANGE", "LISTS", "ITEMS"]


class FunctionCommandDumper(ArgumentAwareCommandInvocationDumper):
    pass


class GetDirectoryPropertyCommandDumper(ArgumentAwareCommandInvocationDumper):
    front_positional_args = 1
    one_value_keywords = ["DIRECTORY", "DEFINITION"]
    back_optional_args = 1


class GetFilenameComponentCommandDumper(ArgumentAwareCommandInvocationDumper):
    front_positional_args = 2
    options = [
        "DIRECTORY",
        "NAME",
        "EXT",
        "NAME_WE",
        "LAST_EXT",
        "NAME_WLE",
        "PATH",
        "PROGRAM",
        "CACHE",
    ]
    one_value_keywords = ["BASE_DIR", "PROGRAM_ARGS"]


class GetPropertyCommandDumper(ArgumentAwareCommandInvocationDumper):
    front_positional_args = 1
    options = ["GLOBAL", "VARIABLE", "SET", "DEFINED", "BRIEF_DOCS", "FULL_DOCS"]
    one_value_keywords = [
        "TARGET",
        "SOURCE",
        "INSTALL",
        "TEST",
        "CACHE",
        "PROPERTY",
    ]
    multi_value_keywords = ["DIRECTORY"]


class IncludeCommandDumper(ArgumentAwareCommandInvocationDumper):
    front_positional_args = 1
    options = ["OPTIONAL", "NO_POLICY_SCOPE"]
    one_value_keywords = ["RESULT_VARIABLE"]


class MacroCommandDumper(ArgumentAwareCommandInvocationDumper):
    pass


class MarkAsAdvancedCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = ["CLEAR", "FORCE"]


class MathCommandDumper(ArgumentAwareCommandInvocationDumper):
    one_value_keywords = ["OUTPUT_FORMAT"]
    multi_value_keywords = ["EXPR"]


class MessageCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = [
        "FATAL_ERROR",
        "SEND_ERROR",
        "WARNING",
        "AUTHOR_WARNING",
        "DEPRECATION",
        "NOTICE",
        "STATUS",
        "VERBOSE",
        "DEBUG",
        "TRACE",
    ]


class SeparateArgumentsCommandDumper(ArgumentAwareCommandInvocationDumper):
    pass


class SetPropertyCommandDumper(ArgumentAwareCommandInvocationDumper):
    options = ["GLOBAL", "APPEND", "APPEND_STRING"]
    one_value_keywords = ["DIRECTORY"]
    multi_value_keywords = ["TARGET", "SOURCE", "INSTALL", "TEST", "CACHE", "PROPERTY"]
