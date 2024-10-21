# Bug Report: Video Download Issue on [Website Name]

## Overview

As a student using **[[100.devs](https://app.100xdevs.com/home)]**, I encountered an issue when attempting to download course videos. The videos are downloaded in multiple `.ts` file segments (e.g., `a1.ts`, `a2.ts`, etc.), but they are not automatically combined into a single video file for seamless viewing. This bug disrupts the user experience as the video remains in multiple fragmented parts.

## Bug Description

- **Bug**: Videos are downloaded in `.ts` chunks but are not combined into a single video.
- **Affected Users**: Students attempting to download full course videos.
- **Steps to Reproduce**:
  1. Navigate to the course video download section.
  2. Initiate the download process.
  3. The video downloads as multiple `.ts` files (e.g., `a1.ts`, `a2.ts`, `a3.ts`, etc.).
  4. The expected behavior is for the video to be combined into one file, but this does not occur.

## Impact

This bug significantly affects the user experience, making it difficult for students to watch the videos without additional technical steps to manually combine them.

## Suggested Solution

A fix is required that combines all `.ts` segments into a single video file automatically upon download. A common solution for combining `.ts` files is using tools like `ffmpeg`, but this should ideally be handled server-side or by the download script.

### Temporary Workaround

For users encountering this issue, here’s a quick solution to manually combine the `.ts` segments:

1. Ensure that all `.ts` files are saved in the same folder.
2. Use the following `ffmpeg` command to merge the segments:

    ```bash
    ffmpeg -f concat -safe 0 -i <(for f in *.ts; do echo "file '$f'"; done) -c copy output_video.mp4
    ```

    This will combine all `.ts` files in the folder into a single `output_video.mp4` file.

## Additional Notes

- This issue may affect a large number of students and should be addressed as a high priority.
- It would be helpful to streamline the download process so students can focus on their learning, rather than handling technical issues.
- If further technical support is needed, please feel free to reach out!

## Contact

If you need more details or clarification on the bug, please contact me at: [Your Email].

---

Thank you for your prompt attention to this issue! 🙏
