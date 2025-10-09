import platform

def safe_import(name):
    try:
        mod = __import__(name)
        return mod, None
    except Exception as e:
        return None, e

def main():
    print("=== Environment sanity check ===")
    print("Python:", platform.python_version())

    torch, err = safe_import("torch")
    if err:
        print("Torch: FAILED ->", err)
    else:
        print("Torch version:", torch.__version__)
        print("CUDA available:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("CUDA device:", torch.cuda.get_device_name(0))

    openslide, err = safe_import("openslide")
    if err:
        print("OpenSlide: FAILED ->", err)
    else:
        print("OpenSlide version:", openslide.__library_version__)

    PIL_Image = None
    pil, err = safe_import("PIL")
    if err:
        print("PIL (Pillow): FAILED ->", err)
    else:
        from PIL import Image as PIL_Image
        PIL_Image.new("RGB", (64, 64)).resize((32, 32))
        print("PIL OK")

    ok = (torch is not None) and (PIL_Image is not None) and (openslide is not None)
    print("=== Result:", "✅ Environment looks good!" if ok else "⚠️  Some checks failed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
