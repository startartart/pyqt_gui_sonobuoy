import os
import re
import copy
import shutil
import numpy as np
import librosa
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

from matplotlib import animation
from functools import partial
from scipy.io import wavfile
from librosa import display as libdis

BASE_PARAMS = {}

def denorm(x):
    return (x * (2**15)).astype(np.int16)

def norm(x):
    max_val = np.max(np.abs(x))
    norm_data = x / max_val
    return norm_data

# 백색잡음(Additive White Gaussian Noise) 부가 함수
def add_awgn(org_signal, snr):
    NL = np.log10(np.sum( org_signal**2 )) - (snr/10)
    NL = np.power(10, NL)
    var = NL / len(org_signal)
    temp = np.random.normal(0, np.sqrt(var), len(org_signal))

    org_signal += temp
    return org_signal


# 시뮬레이터로 생성한 이진 파일을
# 오디오 파일로 변환하여 각자 파일에 저장
def convert_to_wav(filepath, savepath, sr=31250, plot=True):
    f = open(filepath)
    filename = filepath.split('\\')[-1][:-4]
    rectype = np.dtype(np.float32)
    org_data = np.fromfile(f, dtype=rectype) # convert from binary file to numpy array
    norm_data = norm(org_data)
    norm_data = add_awgn(norm_data, 20)
    # save wav file
    wavfile.write(os.path.join(savepath, filename + '.wav'), rate=sr, data=denorm(norm_data))

    # plot if True
    if plot:
        # time domain
        xticks = np.arange(len(org_data))/sr
        fig, axes = plt.subplots(2, 1, figsize=(15,10))
        axes[0].plot(xticks, org_data)
        axes[0].set_title('Original Signal')
        axes[0].set(xlabel='time(sec)', ylabel='Amplitude')
        axes[1].plot(xticks, norm_data)
        axes[1].set_title('Normalized Signal')
        axes[1].set(xlabel='time(sec)', ylabel='Amplitude')
        # fig.savefig(os.path.join(savepath, filename + '.png'))
        fig.savefig('wav.png')
        del fig, axes
        # freq domain
        fig, ax = plt.subplots(1, 1, figsize=(15,8))
        S = librosa.stft(norm_data)
        S_dB = librosa.amplitude_to_db(np.abs(S))
        # timestep = np.ceil(len(norm_data)/(2048/4), dtype=np.int32) # timestep의 계산
        libdis.specshow(S_dB, sr=sr, x_axis='time', y_axis='hz', ax=ax)
        ax.set_title('Normalized Signal Spectrogram')
        # fig.savefig(os.path.join(savepath, filename + '_Spec.png'))
        fig.savefig('./Spec.png')


def load_data(x, dtype):
    # read data from binary files
    if isinstance(x, list):
        data = []
        for f in x:
            data.append(np.fromfile(f, dtype))
    else:
        data = np.fromfile(x, dtype=dtype)

    return data

def get_params_single(n_param, description, pattern):
    params = []
    print(f"{description}/종료를 원할 시 \'exit\' 입력")
    cnt = 0
    scanner = partial(re.match, pattern=pattern)
    while (True):
        s = input(f'{cnt+1}번째 입력 : ')
        if s == 'exit': break  # 종료
        # 올바른 입력일 시 추가
        if scanner(string=s):
            params.append(s+'\n')
            cnt += 1
        else:  # 양식에 맞지않은 입력일 시
            print('양식에 맞추어 입력해 주세요')
            continue

    assert cnt == len(params)

    return params

def get_params_multiple(n_param, description, pattern):
    params = []
    print(f"{description}")
    cnt = 0
    scanner_main = partial(re.match, pattern=pattern)
    scanner_sub = partial(re.match, pattern='[0-9]+$')
    while(True):
        sub_param = []
        sub_cnt = 0
        num = input(f'\n{cnt+1}번째 실험에 입력될 {n_param}의 수 입력\n종료를 원할 시 \'exit\' 입력')

        if num == 'exit' : break

        if scanner_sub(string=num) == None:
            print('양식에 맞추어 입력해 주세요')
            continue

        while(sub_cnt < int(num)):
            s = input(f'{cnt+1}번째 실험 {sub_cnt+1}번 입력 :')
            if scanner_main(string=s):
                sub_param.append(s+'\n')
                sub_cnt += 1
            else:
                print('양식에 맞추어 입력해 주세요')
                continue

        params.append(sub_param)
        cnt += 1

    return params

def get_sim_params():
    # get parameter name
    c_param = input('조정할 파라미터명을 입력해 주세요 ex) depth, tx, rx 등... : ')
    # 코드에 없는 파라미터 입력시 탈출
    if c_param not in list(BASE_PARAMS.keys()) : raise ValueError('존재하지 않는 파라미터입니다')
    # 출력될 파라미터 모음 정의
    params = []
    # 각 파라미터별 처리
    if c_param in ['rx', 'tx', 'target']:
        params = get_params_single(c_param,
                            "좌표 입력(x, y, z)/ex) \'100 500 8\'",
                            '[0-9]+\s[0-9]+\s[0-9]+$')
    elif c_param == 'depth':
        params = get_params_single(c_param,
                            "수심 정보 입력/ex) \'300\'",
                            '[0-9]+$')
    elif c_param == 'pulse':
        params = get_params_single(c_param,
                                   "pulse type duration[ms] freq[Hz] bandwidth[Hz], type : 1 = CW, 2 = LFM/ex) \'2 100 7000 400\'",
                                   '[1-2]\s[0-9]+\s[0-9]+\s[0-9]+$')
    elif c_param == 'sl':
        params = get_params_single(c_param,
                                   "sl (source level)/ex) \'230\'",
                                   '[0-9]+$')
    elif c_param == 'range':
        params = get_params_single(c_param,
                                   "range (거리 파라미터) min max step, 단위[m] min에서 max까지 ray tracing 수행/ex) \'0 15000 10\'",
                                   '[0-9]+\s[0-9]+\s[0-9]+$')
    elif c_param == 'azimuth':
        params = get_params_single(c_param,
                                   "azimuth (방위각 파라미터) min max step, 단위 [deg]/ex) \'0 360 10\'",
                                   '[0-9]+\s[0-9]+\s[0-9]+$')
    elif c_param == 'svp':
        params = get_params_multiple(c_param,
                                     "svp (sound velocity profile, 수심음속)",
                                     '[0-9]+\s[0-9]+$')
    elif c_param == 'highlight':
        params = get_params_multiple(c_param,
                                     "highlight (target highlight)\n각 좌표는 중심에 대한 상대적인 좌표임. 표적의 aspect에 따라 자동 계산됨.",
                                     '[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+$')
    else:
        raise ValueError('존재하지 않는 파라미터 입니다.')

    print(f'종료.\n실험할 파라미터 명 : {c_param}\n실험 시뮬레이션 수 : {len(params)}')

    return c_param, params


def scan_params(lines):
    scanner = partial(re.match, pattern="[a-zA-Z]+\s")
    cnt = 0
    for i, l in enumerate(lines):

        if cnt > 0:
            continue

        compile = scanner(string=l)
        if compile:
            if l.split(' ')[0] in ['svp', 'highlight']:
                BASE_PARAMS[compile.group(0)[:-1]] = lines[i+1:i+1+int(l.split(' ')[-1])]
            else:
                BASE_PARAMS[compile.group(0)[:-1]] = l[compile.span()[1]:]

def main(paramList):
    global BASE_PARAMS
    base_dir = '.\\output'
    generator_path = '.\\Release\\ActiveSigGen.exe'
    isPlotly = True
    saveTracing = True

    # 베이스 파일 읽어오기
    with open('example.txt') as f:
        lines = f.readlines()

    # 검사
    scan_params(lines)

    # 파라미터 받아오기
    n_param, params = get_sim_params()
    # n_param= 'pulse'
    print(n_param, params)

    # 디렉토리 생성
    output_dir = os.path.join(base_dir, f'{n_param}_{len(params)}')
    os.makedirs(output_dir, exist_ok=True)

    coords = {}
    coords['tx'] = paramList['tx']
    coords['rx'] = paramList['rx']
    coords['target'] = paramList['target']
    coords['depth'] = paramList['depth']

    # params = [1,3000,3000,3000]
    # coords['tx'] = int(0)
    # coords['rx'] = [int(x) for x in BASE_PARAMS['rx'].strip().split(' ')]
    # coords['target'] = [int(x) for x in BASE_PARAMS['target'].strip().split(' ')]
    # coords['depth'] = int(BASE_PARAMS['depth'].strip())

    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j] # tx, rx, target에 구(sphere)형의 점을 plot하기 위함

    # 실험 진행
    for i, param in enumerate(params):
        file_path = os.path.join(output_dir, f'sim_{i}.txt')
        file = open(file_path, 'w')

        output_path = os.path.join(output_dir, f'sim_{i}')
        os.makedirs(output_path, exist_ok=True)

        for key in list(BASE_PARAMS.keys()):
            if key == n_param:
                if key in ['svp', 'highlight']:
                    param.insert(0, f'{key} {len(param)}\n')
                    file.writelines(param)
                else:
                    file.write(f'{key} {param}')
            else:
                if key in ['svp', 'highlight']:
                    base_param = copy.deepcopy(BASE_PARAMS)
                    base_param[key].insert(0, f'{key} {len(base_param[key])}\n')
                    file.writelines(base_param[key])
                else:
                    file.write(f'{key} {BASE_PARAMS[key]}')

        # 전송기, 수신기, 표적 상대적 위치를 3차원 plot
        if n_param in ['tx', 'rx', 'target']:
            coords[n_param] = [int(x) for x in param.strip().split(' ')]
        if n_param == 'depth':
            coords[n_param] = int(param.strip())

        # plotly 라이브러리를 사용할 것인지 혹은
        # 일반적인 matplotlib 라이브러리를 사용해 시각화를 할 것인지 여부
        if not isPlotly:
            fig, ax = plt.subplots(1, 1, figsize=(10, 10), subplot_kw={'projection' : '3d'})
            for n, label, c in zip(['tx', 'rx', 'target'],
                                ['Transmitter', 'Receiver', 'Target'],
                                [plt.cm.YlOrBr, plt.cm.RdPu, plt.cm.PuBuGn]):
                # ax.scatter(coords[n][0], coords[n][1], coords[n][2], c=c, label=label)
                x = (0.03*5000) * np.cos(u) * np.sin(v)
                y = (0.03*5000) * np.sin(u) * np.sin(v)
                z = (0.03*coords['depth']) * np.cos(v)
                ax.plot_surface(coords[n][0]+x, coords[n][1]+y, coords[n][2]+z, cmap=c, label=label)
                ax.text(coords[n][0]+5, coords[n][1]+5, coords[n][2]+5, label)

            ax.set_title('Position plot')
            ax.set(xlim=[0, 5000], ylim=[0, 5000], zlim=[0, coords['depth']])
            ax.set(xlabel='X', ylabel='Y', zlabel='Depth')
            fig.savefig(os.path.join(output_dir, f'sim_{i}_pos.png'))

            # 회전 애니메이션
            def animate(i):
                ax.view_init(elev=30., azim=i)
                return fig,

            # animate
            anim = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)

            # save
            anim.save(os.path.join(output_dir, f'sim_{i}_pos.gif'), fps=30)

            del fig, ax, anim

        else:
            # plotly 3차원 plot
            # html 포멧으로 저장
            fig = go.Figure(layout=go.Layout(title=go.layout.Title(text='Relative Position Plot')))
            for n, label, c in zip(['tx', 'rx', 'target'],
                                   ['Transmitter', 'Receiver', 'Target'],
                                   [0, 1, 2]):
                fig.add_trace(go.Scatter3d(
                    x=[coords[n][0]],
                    y=[coords[n][1]],
                    z=[coords[n][2]],
                    mode='markers+text',
                    name=label,
                    text=[label],
                    textposition='top center',
                    marker=dict(size=5,
                                color=c,
                                colorscale='Viridis',
                                opacity=0.8)))

            fig.update_yaxes(autorange='reversed')
            fig.update_layout(
                scene=dict(xaxis=dict(range=[0,15000]),
                           yaxis=dict(range=[0,5000]),
                           zaxis=dict(range=[0,coords['depth']]))
            )

            fig.write_html(os.path.join(output_path, f'sim_{i}_pos.html'))

            del fig

        file.close()
        

        # 생성한 파일을 바탕으로 생성
        print(f'{i+1}번째 시뮬레이션 진행중...')
        print(f'{generator_path} {file_path} .\\{output_path}\\sim_{i}.dat')
        os.system(f'{generator_path} {file_path} .\\{output_path}\\sim_{i}.dat')
        convert_to_wav(f'.\\{output_path}\\sim_{i}.dat', savepath=output_path)
        if saveTracing:
            os.makedirs(os.path.join(output_path, 'Transmitter'), exist_ok=True)
            os.makedirs(os.path.join(output_path, 'Receiver'), exist_ok=True)
            # 수신기, 송신기의 sound ray tracing 데이터를
            # 같은 디렉토리로 옮기기
            tx_files = [x for x in os.listdir('Transmitter') if not x.startswith('.')]
            rx_files = [x for x in os.listdir('Receiver') if not x.startswith('.')]

            assert len(tx_files) > 0 and len(rx_files) > 0, 'There is no Tracing data'

            for t, r in zip(tx_files, rx_files):
                shutil.move(os.path.join('Transmitter', t), os.path.join(output_path, 'Transmitter', t))
                shutil.move(os.path.join('Receiver', r), os.path.join(output_path, 'Receiver', r))

            os.rmdir('Transmitter')
            os.rmdir('Receiver')

        print(coords)
        print('종료!\n')

        #######
        x = [10]
        y = [10]
        z = [10]
        fig = go.Figure(data=[go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                size=12,
                color=z,
                colorscale='Viridis',
                opacity=0.8
            )
        )])
        fig.write_html('test.html')
        data_dir = './output/Receiver'
        data_x = np.fromfile(os.path.join(data_dir, '0_main_x.dat'), dtype='float32')
        data_z = np.fromfile(os.path.join(data_dir, '0_main_z.dat'), dtype='float32')

        data_dir = './output/Transmitter'
        data_dir2 = './output/Receiver'

        tx_files = [x for x in os.listdir(data_dir) if not x.startswith('.')]
        tx_files2 = [x for x in os.listdir(data_dir2) if not x.startswith('.')]

        # sort by index
        tx_files = list(sorted(tx_files, key=lambda x: int(x.split('_')[0])))
        tx_files2 = list(sorted(tx_files2, key=lambda x: int(x.split('_')[0])))

        # add path to files
        tx_files = [os.path.join(data_dir, x) for x in tx_files]
        tx_files2 = [os.path.join(data_dir2, x) for x in tx_files2]

        D_COUNT = 4

        # split data
        total_files = []
        total_files2 = []
        files = []
        files2 = []
        for i, f in enumerate(tx_files):

            if i != 0 and i % D_COUNT == 0:
                total_files.append(files)
                files = []

            files.append(tx_files[i])

        for i, f in enumerate(tx_files2):

            if i != 0 and i % D_COUNT == 0:
                total_files2.append(files2)
                files2 = []

            files2.append(tx_files2[i])

        d = total_files[100]
        d2 = total_files2[100]

        main_x = load_data(d[2], 'float32')
        main_z = load_data(d[3], 'float32')
        main_x2 = load_data(d2[2], 'float32')
        main_z2 = load_data(d2[3], 'float32')

        # plot main sound propagation
        fig, axes = plt.subplots(1, 1, figsize=(20, 10))
        axes.set_title('Main sound propagation', fontsize=24)
        len_z = 0
        for d in total_files[0:380:20]:
            main_x = load_data(d[0], 'float32')
            main_z = load_data(d[1], 'float32')

            max_z = np.max(main_z)
            if max_z > len_z: len_z = max_z
            #     main_z = len_z - main_z

            axes.plot(main_x, main_z)

        axes.invert_yaxis()
        axes.set_xlabel('Range(m)', fontsize=20)
        axes.set_ylabel('Depth(m)', fontsize=20)
        axes.set(yticks=np.arange(0, len_z, 20))

        axes.set(xlim=[0, 9000], ylim=[len_z, 0])
        # axes.set(xlim=[0,3000], ylim=[len_z, 0])
        # axes.invert_xaxis()
        # axes.set(xticks=np.arange(3000, 0, -500))
        # axes.set_xticks([0,500,1000,1500,2000,2500,3000],['3000','2500','2000','1500','1000','500','0'])
        # axes.set_xticks()
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        fig.savefig('./soundpath.png')

# if __name__ == '__main__':
#     main({'depth': 100, 'tx': [100,200,100], 'rx': [100,200,100], 'target': [100,200,100], 'waveType': 2, 'cycle': 100, 'centerFreq': 1000, 'bandwidth': 1000})