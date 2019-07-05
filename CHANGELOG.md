<a name="v3.1.0"></a>
## [v3.1.0](https://github.com/alexseitsinger/package-controller/compare/v3.0.1...v3.1.0) (2019-07-05)

### Code Refactoring
- Adds headers to all sessions. ([0cf3d1d](https://github.com/alexseitsinger/package-controller/commit/0cf3d1db9eab0f0db0b91fd4e6a1184df22048f3))
- Changes for get_config module api. ([9968f65](https://github.com/alexseitsinger/package-controller/commit/9968f65a002bd2204096cacf9f390dad5854b517))
- Read_file uses variable for python only. ([eb0f921](https://github.com/alexseitsinger/package-controller/commit/eb0f921c07db2dac4196994c7d4961e0048dafbc))
- Renames get_package_controller_file. ([f38ca19](https://github.com/alexseitsinger/package-controller/commit/f38ca1964a48cc810565b2a4f19d52d4bb2e02f8))

### Features
- Adds create_personal_repository module. ([2d607d9](https://github.com/alexseitsinger/package-controller/commit/2d607d96a2c4674746d7082d5aaf8a5c7a045d2a))
- Adds gitignore library util module. ([d750d8e](https://github.com/alexseitsinger/package-controller/commit/d750d8ef5781d9895d3b53b6702b8416c1c67784))
- Adds init cli and library command. ([c2b6d52](https://github.com/alexseitsinger/package-controller/commit/c2b6d52ab02c14d503734ef51b4b3eaff3e00479))


<a name="v3.0.1"></a>
## [v3.0.1](https://github.com/alexseitsinger/package-controller/compare/v3.0.0...v3.0.1) (2019-06-30)

### Bug Fixes
- Adds exception handler for empty changelogs. ([918f677](https://github.com/alexseitsinger/package-controller/commit/918f677d0e84414327d3ca8e5a6ae708b8c85661))
- Correctly throws exception. ([df5f56f](https://github.com/alexseitsinger/package-controller/commit/df5f56f007e66a374c21e268fb9c3c79f32ca20d))

### Code Refactoring
- Removes unnecessary argument. ([243a742](https://github.com/alexseitsinger/package-controller/commit/243a742e84a04bad6da759478f12f02b2620c880))
- Removes unused import. ([3c0228f](https://github.com/alexseitsinger/package-controller/commit/3c0228f191a10a92928f973b76d5faa5509dd743))
- Renames authenticated to authorized. ([09855e7](https://github.com/alexseitsinger/package-controller/commit/09855e72159cf09c7875a371951374293eda5805))


<a name="v3.0.0"></a>
## [v3.0.0](https://github.com/alexseitsinger/package-controller/compare/v2.8.0...v3.0.0) (2019-06-30)

### Bug Fixes
- Adds missing - in `release_command`. ([bfa373e](https://github.com/alexseitsinger/package-controller/commit/bfa373eef6665ed4dba7729a91e939ff5d5647f4))
- Adds missing default values for args. ([298744a](https://github.com/alexseitsinger/package-controller/commit/298744a35e438af52558fcc215a414f65014c454))
- Adds missing file deletion in `build`. ([9481417](https://github.com/alexseitsinger/package-controller/commit/948141769ccdc71eb2d3332879b7d66d7afea34c))
- Fixes wheel name format. ([a9ca05c](https://github.com/alexseitsinger/package-controller/commit/a9ca05cd84c3b74099c72b25531770b487f3e7e3))

### Code Refactoring
- Adds return value to release. ([260981c](https://github.com/alexseitsinger/package-controller/commit/260981cb3d19e6b2ff7f18cf9fc64514bd8561ac))
- Changes arguments. ([ce66c23](https://github.com/alexseitsinger/package-controller/commit/ce66c23e0762deafddf10eaaa9f8ba8192682f64))
- Changes get_version to version. ([4c212d6](https://github.com/alexseitsinger/package-controller/commit/4c212d67883d063e1b123e18de5d7fa97845298f))
- Changes to lightweight tags. ([02fa5df](https://github.com/alexseitsinger/package-controller/commit/02fa5df42b2435c788b995416b225dc4ed9b405a))
- Creates new library module import. ([b054716](https://github.com/alexseitsinger/package-controller/commit/b054716ec47bb30454d3326d91f1805e2f4e8322))
- Moves create_release to github library. ([3213566](https://github.com/alexseitsinger/package-controller/commit/3213566c1dc079ea91f741a2cc4fa630f26957a9))
- Moves modules around. ([20e7779](https://github.com/alexseitsinger/package-controller/commit/20e77791b5e4205ec1757c70cabbe353d3d85414))
- Renamed commands. ([16b6760](https://github.com/alexseitsinger/package-controller/commit/16b6760a4264b4de3841f1f12aec5e7c3bb531d6))
- Set draft to False by default. ([5d20700](https://github.com/alexseitsinger/package-controller/commit/5d20700421af31d3c626c2ab631ed63c41616f22))
- Shortened publish command. ([4f3c46a](https://github.com/alexseitsinger/package-controller/commit/4f3c46aaeeeff97f3fbf990f123a2da1ecde577e))
- Updates push. ([be8ba4b](https://github.com/alexseitsinger/package-controller/commit/be8ba4ba66dd434d6abdd8b14b804113295336ea))
- Updates release method. ([414227b](https://github.com/alexseitsinger/package-controller/commit/414227ba81a08d35df2b15593c0c21df297d7c30))

### Features
- Adds `create_release` module. ([fe3a901](https://github.com/alexseitsinger/package-controller/commit/fe3a9014f6e9f0b2496875d5a89dac72b4d548ad))
- Adds `get_latest_changelog` module. ([1239cbf](https://github.com/alexseitsinger/package-controller/commit/1239cbfefd6a0d1419114a7af0a52378887265ef))
- Adds `get_remote_info` git library module. ([cc64687](https://github.com/alexseitsinger/package-controller/commit/cc6468759edb9ecf17511a62fdc62c1f515ebb66))
- Adds generic module. ([6bd4775](https://github.com/alexseitsinger/package-controller/commit/6bd4775c7ab53226f1f05d29453386271125b7e7))
- Adds github library. ([f5c5528](https://github.com/alexseitsinger/package-controller/commit/f5c552819f10ea6dd5bb2619bd80698e9ae2b963))
- Adds prerelease,draft flag options. ([1b4813d](https://github.com/alexseitsinger/package-controller/commit/1b4813d4de7cfaea124b73b4f15f79f70caa7973))


<a name="v2.8.0"></a>
## [v2.8.0](https://github.com/alexseitsinger/package-controller/compare/v2.6.0...v2.8.0) (2019-06-29)

### Bug Fixes
- Attempts to fix no file arg save. ([0cb3035](https://github.com/alexseitsinger/package-controller/commit/0cb3035f7a0856c4e751bf259432e272cef9698a))
- Fixes commit command args. ([20724bb](https://github.com/alexseitsinger/package-controller/commit/20724bb800ad43fe841d0bc3d95a17079bcb1843))
- Fixes missing variables in format call. ([68433e6](https://github.com/alexseitsinger/package-controller/commit/68433e666b907af516926fecb16343d338c26b62))
- Fixes TypeError on None arg. ([54ddde8](https://github.com/alexseitsinger/package-controller/commit/54ddde843a6ecdffba9d479f220bd73e7bdb438b))
- Makes add_file work without args. ([e3933a5](https://github.com/alexseitsinger/package-controller/commit/e3933a53a1dcdcc5b77b4383d88a0b2e4f69314b))

### Code Refactoring
- Adds elif instead of if. ([913d8db](https://github.com/alexseitsinger/package-controller/commit/913d8db62923d242da423112fcdf71938ef9c90c))
- Attempts to fix tag changelog heading. ([07e93ca](https://github.com/alexseitsinger/package-controller/commit/07e93ca23045ab9bac8973c11118034dae5700d2))
- Attempts to fix tag changelog heading. ([59697cb](https://github.com/alexseitsinger/package-controller/commit/59697cb096a72e2cc112839dce784c0dbed1d1b6))
- Fixes heading of tag changelog. ([ca9b555](https://github.com/alexseitsinger/package-controller/commit/ca9b5551c4cd675965d8c3a9285d1062aa4e32ac))
- Fixes tag changelog heading. ([3450f81](https://github.com/alexseitsinger/package-controller/commit/3450f81aeda29cf2283346ce84c009f3fcddf88a))
- Makes file arg optional. ([d72cc08](https://github.com/alexseitsinger/package-controller/commit/d72cc08fa67e65b04d6f09c458b92e8e6295b9a6))
- Makes files arg wild/optional. ([c5761d1](https://github.com/alexseitsinger/package-controller/commit/c5761d1d25d91e0d1fe49c565611f05c227585b6))
- Makes subject,description from one arg. ([b693ee7](https://github.com/alexseitsinger/package-controller/commit/b693ee73da1e7989845faf1b108566a46b6c7f16))
- Removes exception for no file names. ([748b3cd](https://github.com/alexseitsinger/package-controller/commit/748b3cdd8a5fd961f1863670c4ed193e9db9887c))
- Tries to fix heading for tag changelog. ([ab4b1e2](https://github.com/alexseitsinger/package-controller/commit/ab4b1e26a3bdbf0dbc0992b6159672399fe920ea))
- Tries to fix tag changelog heading. ([c1a51d0](https://github.com/alexseitsinger/package-controller/commit/c1a51d031d7b6e91e173a9400c28007358affc63))
- Uses top of changelog. ([5b196c4](https://github.com/alexseitsinger/package-controller/commit/5b196c4fafca02848b7e5053f9f6b356c7b47149))

### Features
- Adds save command. ([4c3773e](https://github.com/alexseitsinger/package-controller/commit/4c3773e98b250a12c099057e7f39f4439b56e8f7))
- Creates annotated tags with git-changelog. ([cf698d4](https://github.com/alexseitsinger/package-controller/commit/cf698d45e092a71701991bbdf64b6a0d38929663))


<a name="v2.6.0"></a>
## [v2.6.0](https://github.com/alexseitsinger/package-controller/compare/v2.5.0...v2.6.0) (2019-06-29)

### Features
- Adds force for git push. ([46eed79](https://github.com/alexseitsinger/package-controller/commit/46eed79b58954d6b076cb53eb8ce22b94bca0469))


<a name="v2.5.0"></a>
## [v2.5.0](https://github.com/alexseitsinger/package-controller/compare/v2.4.0...v2.5.0) (2019-06-28)

### Code Refactoring
- Defaults to create README from src dir. ([639251e](https://github.com/alexseitsinger/package-controller/commit/639251ef39fc64b81c6d21e3b5e47f8bf955c4bd))
- Removes TOC from README. ([595f464](https://github.com/alexseitsinger/package-controller/commit/595f464d9fea540195392e6c48e43c08f74efdfe))
- Trys making docs from dir, then index. ([1ec1cab](https://github.com/alexseitsinger/package-controller/commit/1ec1cab9191b0c9919cf3b40910c8a9fb340b076))

### Features
- Deletes invalid tags before bumping version. ([1d08b29](https://github.com/alexseitsinger/package-controller/commit/1d08b299e246801123405bdad34acc17ca8a4724))


<a name="v2.4.0"></a>
## [v2.4.0](https://github.com/alexseitsinger/package-controller/compare/v2.3.0...v2.4.0) (2019-06-24)

### Bug Fixes
- Fixes import for assert_status. ([9433bb0](https://github.com/alexseitsinger/package-controller/commit/9433bb0e34ec4088db7ba3b53ede1faca769f7be))
- Fixes line counting. ([70a6844](https://github.com/alexseitsinger/package-controller/commit/70a6844c372c585130d115a79e43dd698031199c))

### Code Refactoring
- Adds root_dir argument. ([8bf5bb6](https://github.com/alexseitsinger/package-controller/commit/8bf5bb63f5b0456d178058ce0982a7aac6ff14a3))
- Removes update_documentation() call. ([8f79316](https://github.com/alexseitsinger/package-controller/commit/8f79316a0c6ab349192cf8873732fc456108f5f5))
- Splits method into utils. ([f62a8c0](https://github.com/alexseitsinger/package-controller/commit/f62a8c0ac156782bc4ece16f252adaf55820d868))

### Features
- Adds document command. ([bdc8ac8](https://github.com/alexseitsinger/package-controller/commit/bdc8ac85c04e08faec8c3d39abcc10857cbe9ded))
- Adds git commit when docs are made. ([27e8d9e](https://github.com/alexseitsinger/package-controller/commit/27e8d9ea920ad183aec41f8545f274d68851727a))
- Creates README from src dir as fallback. ([73a4e89](https://github.com/alexseitsinger/package-controller/commit/73a4e8939801ed285beca05209d3d91842d7f173))
- Passes status_message command to fascade. ([2094cb2](https://github.com/alexseitsinger/package-controller/commit/2094cb2310a3369783577b185391ee430a1e923a))


<a name="v2.3.0"></a>
## [v2.3.0](https://github.com/alexseitsinger/package-controller/compare/v2.2.0...v2.3.0) (2019-06-21)

### Bug Fixes
- Finds index file to create docs from. ([7f4d64d](https://github.com/alexseitsinger/package-controller/commit/7f4d64d8954ec2caa4f2eebb4b73ec783a139276))


<a name="v2.2.0"></a>
## [v2.2.0](https://github.com/alexseitsinger/package-controller/compare/v2.1.0...v2.2.0) (2019-06-17)

### Bug Fixes
- Adds check for updating documentation. ([b5294fd](https://github.com/alexseitsinger/package-controller/commit/b5294fdcc719ed971aa0270be81c1ad945807b54))
- Removes non-existent import. ([2107474](https://github.com/alexseitsinger/package-controller/commit/21074741fa0940093fd797829bc2666a41a90183))

### Features
- Makes yarn release non-interactive. ([a63b334](https://github.com/alexseitsinger/package-controller/commit/a63b3342c35ba9be5a9d85045abce40d1682c7d0))


<a name="v2.1.0"></a>
## [v2.1.0](https://github.com/alexseitsinger/package-controller/compare/v2.0.2...v2.1.0) (2019-06-14)

### Features
- Adds documentation to version bump for node. ([a30d889](https://github.com/alexseitsinger/package-controller/commit/a30d889d3a79d0ed3de001d84cac1cc5ca5915e7))
- Adds get_python_package_version util. ([bd1ee7b](https://github.com/alexseitsinger/package-controller/commit/bd1ee7b5887bd3411f47196115f2fa1f75dac9aa))
- Adds pin/unpin commands for node. ([4e93216](https://github.com/alexseitsinger/package-controller/commit/4e93216cb0a7cf67a6f81c3fc1fc4cb9fbaa929b))
- Adds pin/unpin for python. ([294816d](https://github.com/alexseitsinger/package-controller/commit/294816dc4fd1e104e899f43600d9f9403dff9882))
- Adds pipe_commands util. ([7c03221](https://github.com/alexseitsinger/package-controller/commit/7c0322163681b86e71ba7174a11a7e2fa997fb2f))


<a name="v2.0.2"></a>
## [v2.0.2](https://github.com/alexseitsinger/package-controller/compare/v2.0.1...v2.0.2) (2019-06-06)

### Bug Fixes
- Fixes missing commit message for node. ([394cdfe](https://github.com/alexseitsinger/package-controller/commit/394cdfe2e0262e3fd2cc89ae1a58f157668d19f2))

### Code Refactoring
- Only converts to array if string. ([0a7abf9](https://github.com/alexseitsinger/package-controller/commit/0a7abf987a80901a56fbc26b64e91140bfbe8c56))


<a name="v2.0.1"></a>
## [v2.0.1](https://github.com/alexseitsinger/package-controller/compare/v2.0.0...v2.0.1) (2019-06-04)


<a name="v2.0.0"></a>
## [v2.0.0](https://github.com/alexseitsinger/package-controller/compare/v1.2.1...v2.0.0) (2019-06-04)

### Bug Fixes
- Fixes variable named the same as method. ([3b6ad9e](https://github.com/alexseitsinger/package-controller/commit/3b6ad9e73d9002014c1ca7c924176df9c816a8c6))
- Renames util import. ([4d8ec85](https://github.com/alexseitsinger/package-controller/commit/4d8ec8518b1eb38ebbe662e0311c9f6f48a446aa))

### Code Refactoring
- Changes imports from util packages. ([15598db](https://github.com/alexseitsinger/package-controller/commit/15598db3853c19a5ba52d98b770bcf979f10f6c5))
- Imports from library instead of utils. ([9019e7a](https://github.com/alexseitsinger/package-controller/commit/9019e7a042482d4818d847ee7cd02532f0715537))
- Moves utils into own packages. ([4d6be37](https://github.com/alexseitsinger/package-controller/commit/4d6be3747c23da7e1a1c1a8b8efc592a2e0418b9))
- Renames utils to library. ([be1d797](https://github.com/alexseitsinger/package-controller/commit/be1d79759971e0520f74c84557808ed33b76a895))


<a name="v1.2.1"></a>
## [v1.2.1](https://github.com/alexseitsinger/package-controller/compare/v1.2.0...v1.2.1) (2019-06-04)

### Bug Fixes
- Changes `RuntimeError` to `AssertionError`. ([37977cf](https://github.com/alexseitsinger/package-controller/commit/37977cfbfd9599787f3eb4c9a0d734f2e595a3c5))


<a name="v1.2.0"></a>
## [v1.2.0](https://github.com/alexseitsinger/package-controller/compare/v1.1.0...v1.2.0) (2019-06-04)

### Code Refactoring
- Changes `run` commands to single string. ([c259ec3](https://github.com/alexseitsinger/package-controller/commit/c259ec3ee4384151b486dbc1e443f3cf9e8def8c))
- Changes from from `*args` to string. ([2106165](https://github.com/alexseitsinger/package-controller/commit/2106165d222522412cd6a76bff2479e84d0ad689))
- Updates message check for exception. ([f955b96](https://github.com/alexseitsinger/package-controller/commit/f955b964b66b0c5e46746b68f3d3ee6e14cec0ba))

### Features
- Adds extra util methods. ([2215246](https://github.com/alexseitsinger/package-controller/commit/22152460d36f3fe85e66734e685aad309b052e23))


<a name="v1.1.0"></a>
## [v1.1.0](https://github.com/alexseitsinger/package-controller/compare/v1.0.1...v1.1.0) (2019-05-30)

### Bug Fixes
- Uses correct exception. ([d01b3f4](https://github.com/alexseitsinger/package-controller/commit/d01b3f4cc77ba9269086f825f6a6c994b23ae0d3))

### Code Refactoring
- Adds flat argument. ([de521c4](https://github.com/alexseitsinger/package-controller/commit/de521c4558c53265fb8d61e3589bdd4179af92b0))
- Changes option to argument. ([09ea2d3](https://github.com/alexseitsinger/package-controller/commit/09ea2d318e1f41fd57ebe9624022dd0ad9bda6cf))
- Moves git_push into fascade. ([50cd7ca](https://github.com/alexseitsinger/package-controller/commit/50cd7ca79d5c0a1ec72dc47099c114a5f70799e3))
- Only pushes single tags. ([cf317b6](https://github.com/alexseitsinger/package-controller/commit/cf317b6fa16e701607f2ab5bff1cacc5365742e1))

### Features
- Adds git diff command. ([c79040e](https://github.com/alexseitsinger/package-controller/commit/c79040edfe873c119b08731e1bd6b1ee4ce4fce9))
- Adds git repository assertion. ([f0175bd](https://github.com/alexseitsinger/package-controller/commit/f0175bda4bb2dc30d48a290333e76709d4a2facd))


<a name="v1.0.1"></a>
## [v1.0.1](https://github.com/alexseitsinger/package-controller/compare/v1.0.0...v1.0.1) (2019-05-30)

### Code Refactoring
- Adds chore: to commit msg. ([2a4e68c](https://github.com/alexseitsinger/package-controller/commit/2a4e68ce8de90ceb6d3160f9a9750ac5df1287a2))
- Only capitalizes first letter of string. ([14dfb75](https://github.com/alexseitsinger/package-controller/commit/14dfb758a51ddfd7ab2c8ac9628bac8a95e15012))
- Tries multiple filenames for whl/tars. ([7354724](https://github.com/alexseitsinger/package-controller/commit/73547241966a15c4b5998cc4fb418e5e361067a7))
- Updated method. ([45beb12](https://github.com/alexseitsinger/package-controller/commit/45beb12d2cbdd56af39e0b43c8eea09978769b5a))
- Uses new util method. ([dc1ccad](https://github.com/alexseitsinger/package-controller/commit/dc1ccadc1af9d7b2a0316ce41f2a3ac97738f3ab))

### Features
- Adds util. ([2357a3b](https://github.com/alexseitsinger/package-controller/commit/2357a3b6f82e07f1fb301a2551ee82ec7f025dfa))


<a name="v1.0.0"></a>
## [v1.0.0](https://github.com/alexseitsinger/package-controller/compare/v0.6.1...v1.0.0) (2019-05-29)

### Bug Fixes
- Adds return value to exception attempt. ([a3139c5](https://github.com/alexseitsinger/package-controller/commit/a3139c5f200856fd7d00bf639deab2c04a570913))

### Code Refactoring
- Adds pyenv check if its py pkg. ([5a1e871](https://github.com/alexseitsinger/package-controller/commit/5a1e871b207f2ff67fa1da6fdcf7aa29a54e931e))
- Changes exception to assertionerror. ([6e91c7b](https://github.com/alexseitsinger/package-controller/commit/6e91c7bd7e75391b7d486d17222f255b0b6a4e26))
- Changes exception to attributeerror. ([7f5d172](https://github.com/alexseitsinger/package-controller/commit/7f5d17252af2663cfa17e1935f008c212131d7b8))
- Changes import for assert_which. ([2d9dc65](https://github.com/alexseitsinger/package-controller/commit/2d9dc65d55c6fa1f3643c10bdaadb370dcfdfe82))
- Moves assert_which to own module. ([c3d0ca8](https://github.com/alexseitsinger/package-controller/commit/c3d0ca8b9d025565266685a06634215681fcbea9))
- Moves exceptions to module tuple. ([7e230e4](https://github.com/alexseitsinger/package-controller/commit/7e230e45d95574c3f2f7fb9091702f553ea567bb))
- Optimizes method. ([51f2544](https://github.com/alexseitsinger/package-controller/commit/51f254407e3ddf2369238d70dc6668b8133f15b4))

### Features
- Add new util to match staged files. ([12d2a84](https://github.com/alexseitsinger/package-controller/commit/12d2a84411d0b2b2b9610c9ee83bff25c7eb5792))
- Adds raise_exception arg for exceptions. ([70340fe](https://github.com/alexseitsinger/package-controller/commit/70340feeca714bc315b46d419de8320839ee4166))
- Adds test command to cli and utils. ([5594211](https://github.com/alexseitsinger/package-controller/commit/5594211370eaa62302bbb072e4030e42f623a389))
- Adds util module. ([d960ca0](https://github.com/alexseitsinger/package-controller/commit/d960ca04422c105a2a03b65cecab524788a81678))


<a name="v0.6.1"></a>
## [v0.6.1](https://github.com/alexseitsinger/package-controller/compare/v0.6.0...v0.6.1) (2019-05-28)

### Code Refactoring
- Fixes output message for node builds. ([c9641a3](https://github.com/alexseitsinger/package-controller/commit/c9641a3207df188b7d424e6dfbc7ae86fb9a00eb))


<a name="v0.6.0"></a>
## [v0.6.0](https://github.com/alexseitsinger/package-controller/compare/v0.5.1...v0.6.0) (2019-05-28)

### Code Refactoring
- Changes release to fascade. ([76f93a5](https://github.com/alexseitsinger/package-controller/commit/76f93a5d597392e8851e7baf954f26c9bbc8879e))


<a name="v0.5.1"></a>
## [v0.5.1](https://github.com/alexseitsinger/package-controller/compare/v0.5.0...v0.5.1) (2019-05-28)

### Bug Fixes
- Fixes changelog incorrect runtime. ([6057b81](https://github.com/alexseitsinger/package-controller/commit/6057b815c9b062ae87a657a91491f53f6fa90178))
- Fixes if statement. ([41cc25a](https://github.com/alexseitsinger/package-controller/commit/41cc25a7fc9e5ee3ed4d572ebadea2a8b151efe3))
- Fixes misspelled patch method name. ([ecdc9d3](https://github.com/alexseitsinger/package-controller/commit/ecdc9d3e77dff8fa6c6b3d4ab677e6aa031f587a))
- Makes extra commit python-specific. ([8cff3fc](https://github.com/alexseitsinger/package-controller/commit/8cff3fc2e28fd7a2bc9bda1cd78f18f56088f7fa))

### Code Refactoring
- Removes changelog call. ([328db76](https://github.com/alexseitsinger/package-controller/commit/328db76446cdbaac093c14af31edb9e58ac43e67))
- Removes extra cli messages. ([91bc421](https://github.com/alexseitsinger/package-controller/commit/91bc421671bff6761984baacd5b77443b3c7dd72))
- Removes fascade and uses same func. ([e91a808](https://github.com/alexseitsinger/package-controller/commit/e91a8084867c53613c6fd6ee3aa018f0f87e4249))


<a name="v0.5.0"></a>
## [v0.5.0](https://github.com/alexseitsinger/package-controller/compare/v0.4.3...v0.5.0) (2019-05-28)

### Code Refactoring
- Adds return value. ([5b50e1e](https://github.com/alexseitsinger/package-controller/commit/5b50e1eb666490d21c1471bf769a54fb990261d6))
- Changes cli message location. ([eb1162d](https://github.com/alexseitsinger/package-controller/commit/eb1162d91ef3b316318a7aa382339ca01dd49081))
- Changes cli output msg. ([db29c86](https://github.com/alexseitsinger/package-controller/commit/db29c86be48dcb85da6ce18136a592d551de4e41))
- Changes git assertion method name. ([0f6379a](https://github.com/alexseitsinger/package-controller/commit/0f6379a155f97ea0146ebed414cb737b84f29b1d))
- Converts to fascade for node and python. ([c05c07c](https://github.com/alexseitsinger/package-controller/commit/c05c07cf909e2adca6d644cc7da2585b0a8c4154))
- Moves duplicated code to main fascade. ([f16b30b](https://github.com/alexseitsinger/package-controller/commit/f16b30bb0f45b8555dfad4ce68a457a216f9d2eb))
- Moves helper funcs to own modules. ([8e98bba](https://github.com/alexseitsinger/package-controller/commit/8e98bba70cbc75b38c13d84a34b6fc26ab54d41a))
- Moves helper method to its own module. ([c687f45](https://github.com/alexseitsinger/package-controller/commit/c687f459ecc0ab39208ef4d8683ef9235eb314c6))
- Optimizes method. ([6af27d6](https://github.com/alexseitsinger/package-controller/commit/6af27d69e4da3c98c6d7d67b64138d532744feb7))
- Removes encoding statement. ([15f09d9](https://github.com/alexseitsinger/package-controller/commit/15f09d994ecc87f49ad0ac481cc27f4b092cd30a))
- Removes min() around index calc. ([d02be7c](https://github.com/alexseitsinger/package-controller/commit/d02be7cb497e7381fa9a856ca35c4282127d8760))
- Renames module. ([eb1417e](https://github.com/alexseitsinger/package-controller/commit/eb1417e3562b5eaedff9cb1197635ad5ca93e0d6))

### Features
- Adds package type checking utils. ([c88760f](https://github.com/alexseitsinger/package-controller/commit/c88760f72b30e0d6f599040b3c5538fc785cb7a5))
- Moves utils into their own modules. ([681912a](https://github.com/alexseitsinger/package-controller/commit/681912ad8d143b18b4da99bb470735ea3089e1fa))


<a name="v0.4.3"></a>
## [v0.4.3](https://github.com/alexseitsinger/package-controller/compare/v0.4.2...v0.4.3) (2019-05-27)

### Code Refactoring
- Adds changelog before tag. ([f416615](https://github.com/alexseitsinger/package-controller/commit/f416615caa743c620a09e4474a9ae5d30508f958))
- Optimizes method. ([c23d7f1](https://github.com/alexseitsinger/package-controller/commit/c23d7f1bc56e2db3d672c168e58b1532070072f4))
- Removes and replaces custom exceptions. ([5ea1d7c](https://github.com/alexseitsinger/package-controller/commit/5ea1d7c88c6b75f653be80231e1b85fb30d6e5d7))

### Features
- Replaces calls to which with assert_which. ([e5b05fd](https://github.com/alexseitsinger/package-controller/commit/e5b05fdb712691a0fe619f2cbd99bd7dae8b44f9))


<a name="v0.4.2"></a>
## [v0.4.2](https://github.com/alexseitsinger/package-controller/compare/v0.4.1...v0.4.2) (2019-05-27)

### Bug Fixes
- Fixes commits failing with description. ([1a51b92](https://github.com/alexseitsinger/package-controller/commit/1a51b92a7f0afd4be9a12e1c537746fc4ea44509))

### Code Refactoring
- Condenses func into single line. ([9021b13](https://github.com/alexseitsinger/package-controller/commit/9021b139ca9e20772e168be66cb8b4bb0ef974b7))
- Find_file raises exception instead. ([2842fe7](https://github.com/alexseitsinger/package-controller/commit/2842fe7b5f20f2982cd354173a172623309fb23a))
- Optimizes process. ([71f63b3](https://github.com/alexseitsinger/package-controller/commit/71f63b3f1d32c6f6680b031be19dca5f03a06a68))


<a name="v0.4.1"></a>
## [v0.4.1](https://github.com/alexseitsinger/package-controller/compare/v0.4.0...v0.4.1) (2019-05-27)


<a name="v0.4.0"></a>
## [v0.4.0](https://github.com/alexseitsinger/package-controller/compare/v0.3.10...v0.4.0) (2019-05-27)

### Bug Fixes
- renames method name correctly ([0fee27d](https://github.com/alexseitsinger/package-controller/commit/0fee27ddbb8002c1fbb577126fc100ef2818d7a5))
- replaces vars with non reserved words ([3ae87dc](https://github.com/alexseitsinger/package-controller/commit/3ae87dc4e7b255c482464e94e044c9e3d242b36c))

### Code Refactoring
- Adds git_add_file method. ([c36cf70](https://github.com/alexseitsinger/package-controller/commit/c36cf70af4f201b3786233c60f8e20f7e8f80870))
- Adds heading len exception description. ([ee3cfcf](https://github.com/alexseitsinger/package-controller/commit/ee3cfcfb2b9eda46d7e188d8720d4c7ce914d3c5))
- changes imports ([873a00f](https://github.com/alexseitsinger/package-controller/commit/873a00fee8caa4ce0ae523a230cd7616823d94df))
- changes imports ([855d60b](https://github.com/alexseitsinger/package-controller/commit/855d60b20e3f1666e0d832e7ecf9c334dbdd4d99))
- Changes save_file to replace_line. ([8880ae1](https://github.com/alexseitsinger/package-controller/commit/8880ae182ba496e74e4a29054a393c2ecd39d815))
- combines run args together ([73731fd](https://github.com/alexseitsinger/package-controller/commit/73731fd104d0193f0ae1e9bc80bd56119c5b81c5))
- moves nested fns to module scope ([748fe0b](https://github.com/alexseitsinger/package-controller/commit/748fe0b1ffdbaf5d560ee1c61e3a129163297df1))
- Raises error when cant find pkg. ([4fb75e8](https://github.com/alexseitsinger/package-controller/commit/4fb75e8f58fe3b0d6a0ef889e2c2c6a164305239))
- removes description from commit messages ([0e8d405](https://github.com/alexseitsinger/package-controller/commit/0e8d405b709e0e9e3065dd08a937a08a2f175c29))
- removes imports ([a1a65eb](https://github.com/alexseitsinger/package-controller/commit/a1a65eb051b85453b143b1467081600ebb82ae49))
- removes imports ([b1b1f07](https://github.com/alexseitsinger/package-controller/commit/b1b1f075faf1a65230bc647e287aada28d43b013))

### Features
- adds add command to cli ([a276ac8](https://github.com/alexseitsinger/package-controller/commit/a276ac8e4b4348c1c5467a916caa3018d28ef932))
- adds commit cli command ([38a7422](https://github.com/alexseitsinger/package-controller/commit/38a7422c7973b016bd16c10e7404bee76c9c7831))
- adds force flag ([d7045d3](https://github.com/alexseitsinger/package-controller/commit/d7045d37481695faf8777e80840a3a95f77ff50b))
- adds force flag ([e2a7174](https://github.com/alexseitsinger/package-controller/commit/e2a7174fb66086f58fea20c4caf0bffa80e1496a))
- adds force flag opt. changes imports. ([494b4ca](https://github.com/alexseitsinger/package-controller/commit/494b4ca8a6fbef50833f1cee7b30b739ca5398e7))
- adds force flag option ([83bb1c6](https://github.com/alexseitsinger/package-controller/commit/83bb1c6301c06bea1a6b6bb866773bc652659d47))
- adds msg formatting and checking ([cc1b700](https://github.com/alexseitsinger/package-controller/commit/cc1b700befc3341eac822a28f72d0459bddd5037))
- changes imports. adds commands ([018b943](https://github.com/alexseitsinger/package-controller/commit/018b94362633ee1d079bfa13b0d2ef152a2f9a3b))
- imports open from io ([bc4d24e](https://github.com/alexseitsinger/package-controller/commit/bc4d24ea9c43e808f7937c3d7b6bf3519c3546f6))
- updates to use util fn ([2661d7a](https://github.com/alexseitsinger/package-controller/commit/2661d7adfb5f12e2a3d0ff739cb633fb645847b8))


<a name="v0.3.10"></a>
## [v0.3.10](https://github.com/alexseitsinger/package-controller/compare/v0.3.9...v0.3.10) (2019-05-18)

### Bug Fixes
- fixes TypeError throwing ([726dbd5](https://github.com/alexseitsinger/package-controller/commit/726dbd5234844f163547a7dd51943a985b99a742))


<a name="v0.3.9"></a>
## [v0.3.9](https://github.com/alexseitsinger/package-controller/compare/v0.3.8...v0.3.9) (2019-05-18)

### Bug Fixes
- fixes git tag exception catching ([ab98fe9](https://github.com/alexseitsinger/package-controller/commit/ab98fe9ba7be8c12f5db7ad7f366882d743b48d0))


<a name="v0.3.8"></a>
## [v0.3.8](https://github.com/alexseitsinger/package-controller/compare/v0.3.7...v0.3.8) (2019-05-18)


<a name="v0.3.7"></a>
## [v0.3.7](https://github.com/alexseitsinger/package-controller/compare/v0.3.6...v0.3.7) (2019-05-18)

### Bug Fixes
- adds missing colon to try ([d38e24f](https://github.com/alexseitsinger/package-controller/commit/d38e24f5bbd724423db5b9b6bf087ff2cf5d0136))

### Code Refactoring
- added status message if changelog fails ([0239544](https://github.com/alexseitsinger/package-controller/commit/02395447c0232b6baeb0650fd28d55d52c779050))
- adds check for executable ([2e018ac](https://github.com/alexseitsinger/package-controller/commit/2e018acc597997e737d30c322f1215c1801d6225))
- adds new utils method to pakcage scope ([54afe73](https://github.com/alexseitsinger/package-controller/commit/54afe738f5bf0e4683756c02f5c51850d0e3b406))
- adds skip for missing twine ([72daa0d](https://github.com/alexseitsinger/package-controller/commit/72daa0d0b708fd87f0de4741746f77a97c546708))
- changes directory names to python-allowed package names ([afdc461](https://github.com/alexseitsinger/package-controller/commit/afdc4615c22bda8a05eaccbf5ab6dbb9c54c02e7))
- changes output messsage for status ([013554f](https://github.com/alexseitsinger/package-controller/commit/013554f6164aaefef0540749d785501df3290737))
- changes var name, adds check for exec ([c38bb6a](https://github.com/alexseitsinger/package-controller/commit/c38bb6af82b8ca3ff3cc369e71b49d424914b4d8))
- makes initial messages bold ([eb994b6](https://github.com/alexseitsinger/package-controller/commit/eb994b6d7da29550950bfe372dc36185e166eb3a))
- reset version ([336b353](https://github.com/alexseitsinger/package-controller/commit/336b353bcc9c874fac2726f248a023d502f3b77e))

### Features
- adds git reset if tag fails ([b8a59c9](https://github.com/alexseitsinger/package-controller/commit/b8a59c9495a31219a0200fdf9c92d6dfb880f2c1))
- adds new util to check if commits exist ([4817e4a](https://github.com/alexseitsinger/package-controller/commit/4817e4a15c55dcd2894fbb8c2bbc7e0f55799a73))
- adds tag deleting if points to bad commit ([8682397](https://github.com/alexseitsinger/package-controller/commit/8682397486f275c96f2cfc2611b14549e329e346))
- adds which util to check for global executables ([8ce91fd](https://github.com/alexseitsinger/package-controller/commit/8ce91fdab6b0cf67e51a265c4ab1045225ac767a))


<a name="v0.3.6"></a>
## [v0.3.6](https://github.com/alexseitsinger/package-controller/compare/v0.3.5...v0.3.6) (2019-05-17)

### Code Refactoring
- adds git status check to start of function ([e585e42](https://github.com/alexseitsinger/package-controller/commit/e585e42fc67251b6526222b6e288790e7e5510c4))
- adds new utils to package scope ([206b52b](https://github.com/alexseitsinger/package-controller/commit/206b52b71b0256b1885f432f7352d1ba6a7454e1))
- moves body of command to util instead ([fd16980](https://github.com/alexseitsinger/package-controller/commit/fd169808b631ae23dba50875f14199383f5cbe07))

### Features
- adds util for bumping version ([20fd430](https://github.com/alexseitsinger/package-controller/commit/20fd43009f1abfd5d6375cb8d9fe9c36f286d56c))
- adds util for checking status ([804029a](https://github.com/alexseitsinger/package-controller/commit/804029a84916f5ed6ef40107ca9310c8664b0651))


<a name="v0.3.5"></a>
## [v0.3.5](https://github.com/alexseitsinger/package-controller/compare/v0.3.4...v0.3.5) (2019-05-13)

### Code Refactoring
- attempts to fix status check ([4300e2f](https://github.com/alexseitsinger/package-controller/commit/4300e2fb0cfb55911af3b85d67badaed1c6e44ca))
- attempts to fix status check ([9ffc669](https://github.com/alexseitsinger/package-controller/commit/9ffc6691a7edaa9ed4c0c0245ea849437b32c8fb))
- changes command args location ([53ffe80](https://github.com/alexseitsinger/package-controller/commit/53ffe80a7489037add1dc36020ffe14fac4610d4))
- changes commit messages ([63e078f](https://github.com/alexseitsinger/package-controller/commit/63e078f0013216b12cb6044e0b446f2a96fe3311))
- changes output ([15be415](https://github.com/alexseitsinger/package-controller/commit/15be4158248fa9bd90cb80c27798cc2779a68f2c))
- changes output ([0d38602](https://github.com/alexseitsinger/package-controller/commit/0d38602e37c9cb323bec9c478cf1b7aae09a82ef))
- fixes status check ([26a6418](https://github.com/alexseitsinger/package-controller/commit/26a6418af1ba11b4df9c31933769b0c219b31251))

### Features
- adds a check for commit status ([2a285d7](https://github.com/alexseitsinger/package-controller/commit/2a285d74453557e104495af623371cfe9436baaf))


<a name="v0.3.4"></a>
## [v0.3.4](https://github.com/alexseitsinger/package-controller/compare/v0.3.3...v0.3.4) (2019-05-13)

### Code Refactoring
- deletes unused utils ([425a034](https://github.com/alexseitsinger/package-controller/commit/425a0347c896acba12461172304b5894718e1c3d))
- updates cli commands ([b8898f0](https://github.com/alexseitsinger/package-controller/commit/b8898f0c5d0b419e8679edd6ea36e12a25e282ba))
- updates package scope util imports ([6f6c7e1](https://github.com/alexseitsinger/package-controller/commit/6f6c7e1f8622bac335cc2db85a99fa996d3deef0))
- updates util method ([dba49f1](https://github.com/alexseitsinger/package-controller/commit/dba49f1deb45091ec0fe179fa57c590ace749c25))

### Features
- adds util methods ([22e00d5](https://github.com/alexseitsinger/package-controller/commit/22e00d5c6b3ca082a409ea5a7afa317645c09c50))


<a name="v0.3.3"></a>
## [v0.3.3](https://github.com/alexseitsinger/package-controller/compare/v0.3.2...v0.3.3) (2019-05-13)

### Code Refactoring
- changes output ([d92b0fd](https://github.com/alexseitsinger/package-controller/commit/d92b0fdf722f521a24405f59484b6ac1e4a008ba))
- moves method ([6a0305a](https://github.com/alexseitsinger/package-controller/commit/6a0305a2945789a21cd1fb4bf76207bdfff0f1f9))

### Features
- adds util method ([a580195](https://github.com/alexseitsinger/package-controller/commit/a580195efea27ea1ef9fb9722d7f76fb7e63f6f7))


<a name="v0.3.2"></a>
## [v0.3.2](https://github.com/alexseitsinger/package-controller/compare/v0.3.1...v0.3.2) (2019-05-13)


<a name="v0.3.1"></a>
## [v0.3.1](https://github.com/alexseitsinger/package-controller/compare/v0.3.0...v0.3.1) (2019-05-13)

### Bug Fixes
- adds missing comma ([7131ae8](https://github.com/alexseitsinger/package-controller/commit/7131ae89d4553628ba244404540c262534297f13))

### Code Refactoring
- changes defaults ([730d2af](https://github.com/alexseitsinger/package-controller/commit/730d2afb66b6d1b84c7512f52071340e08e207df))


<a name="v0.3.0"></a>
## [v0.3.0](https://github.com/alexseitsinger/package-controller/compare/v0.2.4...v0.3.0) (2019-05-13)

### Code Refactoring
- moves modules ([948f65e](https://github.com/alexseitsinger/package-controller/commit/948f65ea82e43163ea8b446331a7184fcbfe8856))

### Features
- adds new commands ([4ddede1](https://github.com/alexseitsinger/package-controller/commit/4ddede171ce54f19bc344ebecdeae3f47af3afd1))
- adds new utils ([6793416](https://github.com/alexseitsinger/package-controller/commit/6793416d56258f399ceedb2bfd56a00d94db8722))
- imports new commands ([1c65eda](https://github.com/alexseitsinger/package-controller/commit/1c65eda004c23a1575d97de863dcc79dc18f7dcb))


<a name="v0.2.4"></a>
## [v0.2.4](https://github.com/alexseitsinger/package-controller/compare/v0.2.3...v0.2.4) (2019-05-13)

### Bug Fixes
- removes trailing comma ([71c35dd](https://github.com/alexseitsinger/package-controller/commit/71c35dd19d2cd070eb147c9c1caa812e12c2f52f))


<a name="v0.2.3"></a>
## [v0.2.3](https://github.com/alexseitsinger/package-controller/compare/v0.2.2...v0.2.3) (2019-05-12)

### Bug Fixes
- fixes method ([6b3cc89](https://github.com/alexseitsinger/package-controller/commit/6b3cc896c6f8b7533f5c624225de882ceebf12d0))


<a name="v0.2.2"></a>
## [v0.2.2](https://github.com/alexseitsinger/package-controller/compare/v0.2.1...v0.2.2) (2019-05-12)

### Bug Fixes
- fixes files args ([c5fdc08](https://github.com/alexseitsinger/package-controller/commit/c5fdc087eba506c01e598bcace9266e7e5d17ddc))

### Code Refactoring
- adjusts method ([1d553b1](https://github.com/alexseitsinger/package-controller/commit/1d553b167825cd096f3379e0fb40ae849b39a8f8))
- adjusts method ([9f4b877](https://github.com/alexseitsinger/package-controller/commit/9f4b877459c57c550d95c99a8f4465af746d746e))
- changes command ([3186b20](https://github.com/alexseitsinger/package-controller/commit/3186b20b0ea45c201b179abc787b75d68689fc00))
- changes method name ([518790d](https://github.com/alexseitsinger/package-controller/commit/518790d0716bfe32f55c61a9d964208f84aff22b))
- changes method name ([a18db13](https://github.com/alexseitsinger/package-controller/commit/a18db13d53861287bb7da0dc140df2aae3a805c7))
- makes modules ([99dac33](https://github.com/alexseitsinger/package-controller/commit/99dac33dfbf53b2e5e72f782b84cabc7e7348d14))
- moves module ([0544fb7](https://github.com/alexseitsinger/package-controller/commit/0544fb783373bffc76038fb4f77b15438dea1e03))
- moves module ([84d415f](https://github.com/alexseitsinger/package-controller/commit/84d415f795e43aeb278d625c1e6b350d29c060ff))
- optimized method ([f711440](https://github.com/alexseitsinger/package-controller/commit/f711440311f8ceba77e8d45377be02bc622f4d7c))
- optimizes method ([695e53f](https://github.com/alexseitsinger/package-controller/commit/695e53f16f4f692e3258839f111fac972818e9b8))
- removes unused module ([9eeac41](https://github.com/alexseitsinger/package-controller/commit/9eeac417cecb0fd4255f36523bbe20f93e5b6e74))
- updates imports ([91cd00b](https://github.com/alexseitsinger/package-controller/commit/91cd00ba6ad54748df13973ea57f9769df5b445f))

### Features
- adds method ([b5066ab](https://github.com/alexseitsinger/package-controller/commit/b5066ab139aab3d1929af78ec9f81e39e4f19060))
- adds module ([d09eb6b](https://github.com/alexseitsinger/package-controller/commit/d09eb6b0c92c3dfde06e7b4f641c0638c8c5a294))


<a name="v0.2.1"></a>
## [v0.2.1](https://github.com/alexseitsinger/package-controller/compare/v0.2.0...v0.2.1) (2019-05-12)

### Bug Fixes
- fixes git_commit ([8af80ec](https://github.com/alexseitsinger/package-controller/commit/8af80ec49b5a37ae6c63ba7259ada793a60d9369))

### Code Refactoring
- changes commit type ([ffa4104](https://github.com/alexseitsinger/package-controller/commit/ffa4104fd9114765125f138b162be39a1cf27beb))
- removes scope argument ([ffa507c](https://github.com/alexseitsinger/package-controller/commit/ffa507ccfd99acd94a6cdc6e4c94f54fdc51c0d1))


<a name="v0.2.0"></a>
## [v0.2.0](https://github.com/alexseitsinger/package-controller/compare/v0.1.11...v0.2.0) (2019-05-11)

### Bug Fixes
- attempts to fix git commit, v2 ([ec6528d](https://github.com/alexseitsinger/package-controller/commit/ec6528db7c43f6d87295307c7ce7aec65fbb6b9c))
- attempts to fix git_commit function ([6d853f6](https://github.com/alexseitsinger/package-controller/commit/6d853f6c9cd492f29467d2e772e8f0f21a701f94))

### Code Refactoring
- removes unused utils ([a913969](https://github.com/alexseitsinger/package-controller/commit/a913969e74532d91ead7e7445346633b1196d423))
- updates modules ([3d8d75c](https://github.com/alexseitsinger/package-controller/commit/3d8d75ca19f08cc0374ef350b68293a55a013c5d))

### Features
- adds git commands ([99b892e](https://github.com/alexseitsinger/package-controller/commit/99b892ec47a27862c938e4871a989b57ed32650d))
- adds git commands ([b3cc432](https://github.com/alexseitsinger/package-controller/commit/b3cc432e022cd440487d0cf024c6078b67747800))
- adds git updates ([e54e4f1](https://github.com/alexseitsinger/package-controller/commit/e54e4f18e36299325a5d387ee7a1615f655d99b1))


<a name="v0.1.11"></a>
## [v0.1.11](https://github.com/alexseitsinger/package-controller/compare/v0.1.10...v0.1.11) (2019-05-11)

### Code Refactoring
- changed package_setup.py to attempt to use name provided, then fallback to name of package directory ([a74f811](https://github.com/alexseitsinger/package-controller/commit/a74f81112eac80598d2e06c58f9e1061cfe8d9e5))

### Features
- added new util methods ([641bd6f](https://github.com/alexseitsinger/package-controller/commit/641bd6f951664929aa577250d7e686c0280cc5d0))
- renamed exceptions, added new one for util ([2eb2f30](https://github.com/alexseitsinger/package-controller/commit/2eb2f30a45d4b9dd77c52f8e7af1c4d0392b9cc6))


<a name="v0.1.10"></a>
## [v0.1.10](https://github.com/alexseitsinger/package-controller/compare/v0.1.0...v0.1.10) (2019-05-11)


<a name="v0.1.0"></a>
## [v0.1.0](https://github.com/alexseitsinger/package-controller/compare/0609384cdfe7aaa9eb45c32fce00b9d9b58694bb...v0.1.0) (2019-05-03)


